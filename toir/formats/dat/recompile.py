from .items import recompile_items

_RECOMPILERS = [
    recompile_items,
]

def recompile_dat(l7cdir, csvdir, outputdir):
    for recompiler in _RECOMPILERS:
        recompiler(l7cdir, csvdir, outputdir)