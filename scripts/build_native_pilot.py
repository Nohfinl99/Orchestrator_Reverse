"""Build an owner-authored deterministic PE64 fixture; never execute the target.

This writes hand-encoded x64 code, NOT compiler output from the reference C.
Only for static acquisition / a separately authorized isolated runtime pilot.
"""
import argparse
import hashlib
import json
from pathlib import Path
import struct


def image():
    data = bytearray(1024)
    data[:2] = b'MZ'
    struct.pack_into('<I', data, 0x3C, 0x80)
    data[0x80:0x84] = b'PE\0\0'
    struct.pack_into('<HHIIIHH', data, 0x84, 0x8664, 1, 0, 0, 0, 240, 0x22)
    opt = 0x98
    struct.pack_into('<H', data, opt, 0x20B)
    struct.pack_into('<I', data, opt + 4, 512)
    struct.pack_into('<II', data, opt + 16, 0x1000, 0x1000)
    struct.pack_into('<Q', data, opt + 24, 0x140000000)
    struct.pack_into('<II', data, opt + 32, 0x1000, 512)
    struct.pack_into('<HH', data, opt + 40, 6, 0)
    struct.pack_into('<HH', data, opt + 48, 6, 0)
    struct.pack_into('<II', data, opt + 56, 0x2000, 512)
    struct.pack_into('<HH', data, opt + 68, 3, 0x100)
    struct.pack_into('<QQQQ', data, opt + 72, 0x100000, 0x1000, 0x100000, 0x1000)
    struct.pack_into('<I', data, opt + 108, 16)
    struct.pack_into('<II', data, opt + 112, 0x1080, 0x80)
    struct.pack_into('<8sIIIIIIHHI', data, opt + 240,
                     b'.text\0\0\0', 512, 0x1000, 512, 512, 0, 0, 0, 0, 0x60000020)
    # Entry point: xor eax,eax; ret. It is not dispatched by this builder.
    data[0x200:0x203] = bytes.fromhex('31 c0 c3')
    # uint32_t pilot_transform(uint32_t x), Windows x64 argument in ecx:
    # cmp ecx,10; jae high; lea eax,[rcx+7]; ret;
    # high: mov eax,ecx; xor eax,0x5a; ret.
    data[0x210:0x21F] = bytes.fromhex('83 f9 0a 73 04 8d 41 07 c3 89 c8 83 f0 5a c3')
    struct.pack_into('<IIHHIIIIIII', data, 0x280,
                     0, 0, 0, 0, 0x10D0, 1, 1, 1, 0x10A8, 0x10AC, 0x10B0)
    struct.pack_into('<IIH', data, 0x2A8, 0x1010, 0x10C0, 0)
    data[0x2C0:0x2D0] = b'pilot_transform\0'
    name = b'orchestrator_pilot\0'
    data[0x2D0:0x2D0 + len(name)] = name
    return bytes(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if not args.output.is_absolute():
        parser.error('output must be absolute')
    parent = args.output.parent.resolve(strict=True)
    if parent != args.output.parent or args.output.suffix.lower() != '.exe':
        parser.error('use an existing canonical parent and .exe extension')
    raw = image()
    assert len(raw) == 1024
    with args.output.open('xb') as stream:
        stream.write(raw)
        stream.flush()
    stored = args.output.read_bytes()
    if stored != raw:
        raise OSError('readback differs')
    print(json.dumps({'status': 'BUILT_NOT_EXECUTED', 'format': 'PE32+',
                      'architecture': 'x86_64', 'bytes': len(raw),
                      'sha256': hashlib.sha256(raw).hexdigest(),
                      'method': 'HAND_ENCODED_DETERMINISTIC_FIXTURE_NOT_C_COMPILATION',
                      'entry_rva': '0x1000', 'target_function_rva': '0x1010',
                      'target_executions': 0}, sort_keys=True))


if __name__ == '__main__':
    main()
