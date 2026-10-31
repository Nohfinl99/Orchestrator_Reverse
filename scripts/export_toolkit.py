#!/usr/bin/env python3
"""Build deterministic offline exports for the Orchestrator Toolkit.

The skill frontmatter parser intentionally supports only the narrow YAML
authoring profile used by these source files; this is not a general YAML parser.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from typing import Dict, Iterable, List, Tuple
from urllib.parse import unquote


PLUGIN_NAME = "orchestrator-toolkit"
PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
SKILLS = ("orch-cua", "orch-strix", "orch-d810-ng", "orch-microsmt", "orch-ollvm-research")
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SAFE_PLAIN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 _.,;()/+&'!?-]*(?::[A-Za-z0-9_/-][A-Za-z0-9 _.,;()/+&'!?-]*)?$")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SECRET_PATTERNS = (
    re.compile(r"(?i)\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    re.compile(r"(?i)\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|secret[_-]?key)\s*[:=]\s*['\"]?[A-Za-z0-9_./+-]{16,}"),
)
ABS_PATH = re.compile(r"(?<![A-Za-z0-9+.-])(?:[A-Za-z]:\\|[A-Za-z]:/)|(?:/Users/|/home/|/root/|/tmp/)")


class ExportError(Exception):
    pass


def fail(message: str) -> None:
    raise ExportError(message)


def ensure_no_symlink(path: Path) -> None:
    """Reject symlinks/reparse points anywhere in an existing path chain."""
    absolute = Path(os.path.abspath(path))
    chain = list(reversed((absolute, *absolute.parents)))
    for part in chain:
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        except OSError as exc:
            fail(f"cannot inspect path {part}: {exc}")
        attributes = getattr(info, "st_file_attributes", 0)
        reparse = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        if stat.S_ISLNK(info.st_mode) or (reparse and attributes & reparse):
            fail(f"symlink/reparse point is not allowed in input/output path: {part}")


def contained(base: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(base)
        return True
    except ValueError:
        return False


def checked_file(root: Path, relative: str) -> Path:
    path = root / PurePosixPath(relative)
    ensure_no_symlink(path)
    try:
        resolved = path.resolve(strict=True)
    except (FileNotFoundError, OSError) as exc:
        fail(f"required input is missing or unreadable: {relative}: {exc}")
    if not contained(root.resolve(strict=True), resolved):
        fail(f"input escapes plugin root: {relative}")
    if not resolved.is_file():
        fail(f"required input is not a file: {relative}")
    return resolved


def scalar(value: str, field: str, line_no: int) -> str:
    value = value.strip()
    if not value:
        fail(f"frontmatter {field} is empty (line {line_no})")
    if value[0] in "'\"":
        if value[0] != '"':
            fail(f"only JSON double-quoted scalars are supported for {field} (line {line_no})")
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            fail(f"invalid JSON-quoted scalar for {field} (line {line_no})")
        if not isinstance(parsed, str) or "\n" in parsed or "\r" in parsed:
            fail(f"{field} must be a single-line string (line {line_no})")
        return parsed
    if not SAFE_PLAIN.fullmatch(value):
        fail(f"unsupported plain scalar syntax for {field} (line {line_no}); quote it as JSON if needed")
    return value


def parse_frontmatter(text: str, skill: str) -> Tuple[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        fail(f"{skill}/SKILL.md must begin with YAML frontmatter")
    try:
        closing = lines.index("---", 1)
    except ValueError:
        fail(f"{skill}/SKILL.md has no closing frontmatter delimiter")
    values: Dict[str, str] = {}
    for index, line in enumerate(lines[1:closing], start=2):
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            fail(f"unsupported frontmatter syntax in {skill}/SKILL.md line {index}")
        key, raw = line.split(":", 1)
        if key not in ("name", "description") or key in values:
            fail(f"frontmatter in {skill}/SKILL.md must contain only one name and description")
        values[key] = scalar(raw, key, index)
    if set(values) != {"name", "description"}:
        fail(f"frontmatter in {skill}/SKILL.md must contain exactly name and description")
    if values["name"] != skill:
        fail(f"frontmatter name {values['name']!r} does not match folder {skill!r}")
    return values["name"], values["description"]


def validate_links(plugin_root: Path, relative: str, text: str) -> None:
    source = plugin_root / PurePosixPath(relative)
    base = plugin_root.resolve(strict=True)
    for match in MARKDOWN_LINK.finditer(text):
        target = match.group(1).strip().split(None, 1)[0].strip("<>")
        lower = target.lower()
        if lower.startswith("https://") or target.startswith("#"):
            continue
        target_path = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not target_path:
            continue
        if target_path.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:", target_path):
            fail(f"absolute local Markdown link is not allowed in {relative}: {target}")
        candidate = source.parent / Path(target_path.replace("/", os.sep))
        ensure_no_symlink(candidate)
        try:
            resolved = candidate.resolve(strict=True)
        except (FileNotFoundError, OSError):
            fail(f"broken local Markdown link in {relative}: {target}")
        if not contained(base, resolved):
            fail(f"local Markdown link escapes plugin root in {relative}: {target}")
        if not resolved.is_file():
            fail(f"local Markdown link does not target a file in {relative}: {target}")


def validate_content(relative: str, content: bytes) -> str:
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        fail(f"input is not UTF-8: {relative}")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            fail(f"possible credential material found in {relative}")
    if ABS_PATH.search(text):
        fail(f"absolute filesystem path found in {relative}")
    return text


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def zip_bytes(entries: Iterable[Tuple[str, bytes]]) -> bytes:
    from io import BytesIO

    output = BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(entries, key=lambda item: item[0]):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.flag_bits = 0x800
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return output.getvalue()


def validate_archive(data: bytes, expected: Dict[str, bytes], label: str) -> None:
    from io import BytesIO

    with zipfile.ZipFile(BytesIO(data), "r") as archive:
        names = archive.namelist()
        if names != sorted(expected) or len(names) != len(set(names)):
            fail(f"post-build ZIP entry list mismatch: {label}")
        for info in archive.infolist():
            path = PurePosixPath(info.filename)
            mode = info.external_attr >> 16
            if path.is_absolute() or ".." in path.parts or stat.S_ISLNK(mode):
                fail(f"unsafe ZIP entry in {label}: {info.filename}")
            content = archive.read(info)
            if content != expected[info.filename] or sha(content) != sha(expected[info.filename]):
                fail(f"post-build ZIP body digest mismatch: {label}:{info.filename}")


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ensure_no_symlink(path)
    ensure_no_symlink(path.parent)
    fd, temp_name = tempfile.mkstemp(prefix=".toolkit-export-", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def validate_manifest(data: bytes) -> dict:
    try:
        manifest = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        fail(f"plugin.json is not valid UTF-8 JSON: {exc}")
    if not isinstance(manifest, dict):
        fail("plugin.json must be a JSON object")
    if manifest.get("name") != PLUGIN_NAME or manifest.get("$schema") != PLUGIN_SCHEMA:
        fail("plugin.json must declare name orchestrator-toolkit and the Agent Plugins 1.0 schema URL")
    if not isinstance(manifest.get("version"), str) or not SEMVER.fullmatch(manifest["version"]):
        fail("plugin.json version must be semantic version X.Y.Z")
    if {"skills", "mcpServers", "apps", "interface"} & set(manifest):
        fail("plugin.json contains a forbidden top-level field")
    extensions = manifest.get("extensions", {})
    if not isinstance(extensions, dict):
        fail("plugin.json extensions must be an object")
    openai = extensions.get("com.openai", {})
    if not isinstance(openai, dict):
        fail("plugin.json extensions.com.openai must be an object")
    interface = openai.get("interface")
    if not isinstance(interface, dict):
        fail("plugin.json extensions.com.openai.interface must be an object")
    short = interface.get("shortDescription")
    if short is not None and (not isinstance(short, str) or len(short) > 30):
        fail("extensions.com.openai.interface.shortDescription must be a string of at most 30 characters")
    if interface.get("category") != "Developer Tools":
        fail("OpenAI interface category must be Developer Tools")
    if not isinstance(interface.get("capabilities"), list):
        fail("extensions.com.openai.interface.capabilities must be an array")
    serialized = json.dumps(manifest, ensure_ascii=False).lower()
    if any(token in serialized for token in ("mcp://", "sse://", "endpoint", "server_url")):
        fail("plugin.json must not declare MCP endpoints")
    return manifest


def build(root: Path, output: Path | None = None) -> Path:
    root = Path(os.path.abspath(root))
    ensure_no_symlink(root)
    if not root.is_dir():
        fail(f"public repository root is not a directory: {root}")
    public_root = root.resolve(strict=True)
    plugin = root / "plugins" / PLUGIN_NAME
    ensure_no_symlink(plugin)
    if not plugin.is_dir():
        fail(f"plugin source directory does not exist: {plugin}")
    plugin_real = plugin.resolve(strict=True)

    package_files = ["plugin.json"]
    for skill in SKILLS:
        package_files += [f"skills/{skill}/SKILL.md", f"skills/{skill}/references/source.md"]
    auxiliary = {"README.md", "PORTABLE_INSTRUCTIONS.txt"}
    source: Dict[str, bytes] = {}
    texts: Dict[str, str] = {}
    for rel in package_files + ["PORTABLE_INSTRUCTIONS.txt"]:
        path = checked_file(plugin, rel)
        raw = path.read_bytes()
        source[rel] = raw
        texts[rel] = validate_content(rel, raw)
    readme = plugin / "README.md"
    if readme.exists():
        path = checked_file(plugin, "README.md")
        raw = path.read_bytes()
        source["README.md"] = raw
        validate_content("README.md", raw)

    actual = set()
    for item in plugin_real.rglob("*"):
        ensure_no_symlink(item)
        if item.is_file():
            actual.add(item.relative_to(plugin_real).as_posix())
    expected = set(package_files) | {"PORTABLE_INSTRUCTIONS.txt"}
    if not expected.issubset(actual) or actual - expected - auxiliary:
        fail("plugin tree violates its whitelist; "
             f"extra={sorted(actual - expected - auxiliary)}, missing={sorted(expected - actual)}")

    manifest_data = validate_manifest(source["plugin.json"])
    for skill in SKILLS:
        rel = f"skills/{skill}/SKILL.md"
        parse_frontmatter(texts[rel], skill)
        validate_links(plugin_real, rel, texts[rel])
        validate_links(plugin_real, f"skills/{skill}/references/source.md",
                       texts[f"skills/{skill}/references/source.md"])

    if output is None:
        destination = root.parent / "local-runs" / "platform-sync-export"
    else:
        destination = output if output.is_absolute() else Path.cwd() / output
    destination = Path(os.path.abspath(destination))
    ensure_no_symlink(destination)
    destination_real = destination.resolve(strict=False)
    if contained(public_root, destination_real):
        fail("output path must be outside the public repository")

    exports: Dict[str, bytes] = {}
    plugin_entries = {f"{PLUGIN_NAME}/{name}": source[name] for name in package_files}
    plugin_zip_name = f"{PLUGIN_NAME}-{manifest_data['version']}.zip"
    exports[plugin_zip_name] = zip_bytes(plugin_entries.items())
    validate_archive(exports[plugin_zip_name], plugin_entries, plugin_zip_name)

    for skill in SKILLS:
        prefix = f"skills/{skill}/"
        entries = {f"{skill}/{name[len(prefix):]}": data for name, data in source.items()
                   if name.startswith(prefix)}
        zip_name = f"{skill}.zip"
        exports[zip_name] = zip_bytes(entries.items())
        validate_archive(exports[zip_name], entries, zip_name)
        skill_text = texts[f"skills/{skill}/SKILL.md"]
        source_text = texts[f"skills/{skill}/references/source.md"]
        flattened = (f"# {skill}\n\n## SKILL.md\n\n{skill_text.rstrip()}\n\n"
                     f"## references/source.md\n\n{source_text.rstrip()}\n")
        exports[f"knowledge/{skill}.txt"] = flattened.encode("utf-8")

    exports["knowledge/Instructions.txt"] = source["PORTABLE_INSTRUCTIONS.txt"]
    manifest_files = []
    for name, data in sorted(source.items()):
        manifest_files.append({"kind": "source", "path": name, "sha256": sha(data), "size": len(data)})
    for name, data in sorted(exports.items()):
        manifest_files.append({"kind": "export", "path": name, "sha256": sha(data), "size": len(data)})
    export_manifest = {
        "format": "orchestrator-toolkit-export-manifest-v1",
        "plugin": PLUGIN_NAME,
        "version": manifest_data["version"],
        "files": manifest_files,
    }
    exports["manifest.json"] = (json.dumps(export_manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")

    destination.mkdir(parents=True, exist_ok=True)
    ensure_no_symlink(destination)
    if contained(public_root, destination.resolve(strict=True)):
        fail("output path resolved inside the public repository")
    # Fixed filenames only; unrelated files already in the destination remain untouched.
    for name, data in sorted(exports.items()):
        atomic_write(destination / Path(*PurePosixPath(name).parts), data)
    return destination


def main(argv: List[str] | None = None) -> int:
    script_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Validate and export the Orchestrator Toolkit (standard library only).")
    parser.add_argument("--root", type=Path, default=script_root,
                        help="public repository root (defaults to the parent of this script's scripts directory)")
    parser.add_argument("--output", type=Path,
                        help="export directory (must resolve outside the public repository; existing files are overwritten by name)")
    args = parser.parse_args(argv)
    try:
        destination = build(args.root, args.output)
    except (ExportError, OSError, zipfile.BadZipFile) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    sys.stdout.buffer.write((str(destination) + "\n").encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
