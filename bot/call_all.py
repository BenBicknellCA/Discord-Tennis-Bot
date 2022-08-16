from matches import get_liveline, live, sched


def call_all():
    sched()
    if live() is not None:
        get_liveline()
        live()
