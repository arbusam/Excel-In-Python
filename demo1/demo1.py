# https://openpyxl.readthedocs.io/en/stable/
from openpyxl import Workbook, load_workbook
from .includes import *

filename = "videos.xlsx"


def start():
    wb = Workbook()

    ws = wb.active
    ws.title = "Video List"
    
    ws = populate_headings(ws, headings)
    ws = populate_data(ws, data)

    wb.save(filename=filename)