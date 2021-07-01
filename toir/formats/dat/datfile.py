import struct
from collections import namedtuple

DatSection = namedtuple('DatSection', ['offset', 'size'])

class DatFile:
    def __init__(self, f):
        self._f = f
        binary = self._f.read(16)
        self.count, = struct.unpack_from('<L', binary, 0)
        header = self._f.read(self.count * 8)
        self.sections = []
        for i in range(self.count):
            offset, size = struct.unpack_from('<LL', header, i * 8)
            self.sections.append(DatSection(offset, size))

    def read_section(self, i):
        self._f.seek(self.sections[i].offset)
        return self._f.read(self.sections[i].size)