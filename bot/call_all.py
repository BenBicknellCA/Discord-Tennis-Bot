from .matches import get_liveline, live, sched

sched()
if live() is not None:
    get_liveline()
    live()
