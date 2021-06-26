from .artes import extract_artes
from .items import extract_items

_EXTRACTORS = [
    extract_items,
    extract_artes,
]

def extract_dat(l7cdir, outputdir):
    for extractor in _EXTRACTORS:
        extractor(l7cdir, outputdir)