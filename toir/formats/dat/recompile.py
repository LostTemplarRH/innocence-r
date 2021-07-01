from .items import recompile_items
from .artes import recompile_artes

_RECOMPILERS = [
    recompile_items,
    recompile_artes,
]

def recompile_dat(l7cdir, csvdir, outputdir):
    for recompiler in _RECOMPILERS:
        recompiler(l7cdir, csvdir, outputdir)