from .artes import extract_artes
from .items import extract_items
from .battlebook import extract_battle_book
from .charaability import extract_chara_ability

_EXTRACTORS = [
    extract_items,
    extract_artes,
    extract_battle_book,
    extract_chara_ability,
]

def extract_dat(l7cdir, outputdir):
    for extractor in _EXTRACTORS:
        extractor(l7cdir, outputdir)