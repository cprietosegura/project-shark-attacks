
import re

def other_activity(e):
    categoría= 'Other activity'
    if re.search(r"[Ss]urf[\sib]", e) == None:
        e=categoría
    return e

def surf_related(e):
    categoría= 'Surf related'
    if re.search(r"[Ss]urf[\sib]", e)!= None:
        e=categoría
    return e