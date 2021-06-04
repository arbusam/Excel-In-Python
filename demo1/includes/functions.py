from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment, PatternFill
from .data import *

def populate_headings(ws, values):
    """Populates the heading for a given worksheet

    Args:
        ws (Worksheet): Worksheet object
        values (List): List of dictionaries

    Returns:
        List: List of headings
    """
    return_value = []
    for heading in headings:
        return_value.append(heading["name"])
    return return_value