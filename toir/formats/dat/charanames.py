from .datfile import DatFile
import struct
import io
from ...text import decode_text
import csv

def write_csv_data(f, format, col_names, data):
    writer = csv.DictWriter(f, col_names)
    if format[0] == 'i':
        if isinstance(data, list):
            for i, value in enumerate(data):
                writer.writerow({
                    col_names[0]: i,
                    col_names[-1]: value,
                })
        elif isinstance(data, dict):
            for i, value in data.items():
                writer.writerow({
                    col_names[0]: i,
                    col_names[-1]: value,
                })

def read_chara_names(l7cdir):
    with open(l7cdir / '_Data/Field/PackFieldData.dat', 'rb') as f:
        binary = f.read()
    dat = DatFile(io.BytesIO(binary))
    
    namesdat = dat.read_section(30)
    count, = struct.unpack_from('<H', namesdat, 0)
    names = []
    for i in range(count):
        names.append(decode_text(namesdat, 2 + i * 0x24))

    section = dat.read_section(32)
    count, = struct.unpack_from('<H', section, 0)
    locations = []
    for i in range(count):
        locations.append(decode_text(section, 2 + i * 0x30))
    return names, locations

def extract_chara_names(l7cdir, outputdir):
    names, locations = read_chara_names(l7cdir)
    with open(outputdir / 'CharaNames.csv', 'w', encoding='utf-8', newline='') as f:
        write_csv_data(f, 'i', ['index', 'japanese'], names)
    with open(outputdir / 'Locations.csv', 'w', encoding='utf-8', newline='') as f:
        write_csv_data(f, 'i', ['index', 'japanese'], locations)