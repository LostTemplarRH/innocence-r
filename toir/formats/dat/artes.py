from .sections import read_sections
import struct
from ...text import decode_text
import csv

def read_artes(section):
    count, = struct.unpack_from('<L', section, 0)
    items = []
    for i in range(count):
        name = decode_text(section, 4 + i * 0xE0 + 0x24)
        description = decode_text(section, 4 + i * 0xE0 + 0x4D)
        items.append({
            'name': name,
            'description': description,
        })
    return items

def _extract_artes(binary):
    artes = {}
    sections = read_sections(binary)
    for i in range(0, len(sections)):
        artes[i] = read_artes(sections[i])
    return artes

def extract_artes(l7cdir, outputdir):
    with open(l7cdir / '_Data/System/ArtsDataPack.dat', 'rb') as f:
        binary = f.read()
    items = _extract_artes(binary)
    with open(outputdir / 'ArtsDataPack.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, ['category', 'index', 'field', 'text'])
        for category, items in items.items():
            for i, item in enumerate(items):
                writer.writerow({
                    'category': category,
                    'index': i,
                    'field': 'name',
                    'text': item['name'],
                })
                writer.writerow({
                    'category': category,
                    'index': i,
                    'field': 'description',
                    'text': item['description'],
                })