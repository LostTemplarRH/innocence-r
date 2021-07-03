from .artes import extract_artes
from .items import extract_items
from .battlebook import extract_battle_book
from .charaability import extract_chara_ability
from .charanames import extract_chara_names
from .tutorial import extract_tutorial
from .mission import extract_mission

_EXTRACTORS = [
    extract_items,
    extract_artes,
    extract_battle_book,
    extract_chara_ability,
    extract_chara_names,
    extract_tutorial,
    extract_mission,
]

def extract_dat(l7cdir, outputdir):
    for extractor in _EXTRACTORS:
        extractor(l7cdir, outputdir)