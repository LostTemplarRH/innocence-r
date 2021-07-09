from .datfile import DatFile
from ...text import decode_text, remove_redundant_cc
from ...csvhelper import write_csv_data
import struct

def _extract_chara_styles(f):
    dat = DatFile(f)
    section = dat.read_section(1)
    count, = struct.unpack_from('<L', section, 0)
    styles = [decode_text(section, 4 + 0x8A * i) for i in range(count)]
    return styles

def extract_chara_styles(l7cdir, outputdir):
    with open(l7cdir / '_Data/System/CharaStyleDataPack.dat', 'rb') as f:
        styles = _extract_chara_styles(f)
    with open(outputdir / 'CharaStyleDataPack.csv', 'w', encoding='utf-8', newline='') as f:
        write_csv_data(f, 'is', ['index', 'japanese'], styles)
