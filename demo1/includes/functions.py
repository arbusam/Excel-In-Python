from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment, PatternFill
from .data import *

def populate_headings():
    return_value = []
    for heading in headings:
        return_value.append(heading["name"])
    return return_value