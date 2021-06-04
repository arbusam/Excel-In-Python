from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl import Workbook, load_workbook
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
    for i in range(len(values)):
        ws[get_column_letter(i+1) + "1"] = values[i]["name"]
    return ws