import struct

def read_sections(binary):
    count, = struct.unpack_from('<L', binary, 0)
    sections = []
    for i in range(count):
        offset, size = struct.unpack_from('<LL', binary, 0x10 + i * 8)
        sections.append(binary[offset:offset+size])
    return sections

def read_dat_header(binary):
    first_offset, = struct.unpack_from('<L', binary, 0x10)
    return binary[:first_offset]