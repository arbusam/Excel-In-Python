# https://openpyxl.readthedocs.io/en/stable/
from openpyxl import Workbook, load_workbook
from .includes import *

data = {
    "ID": [1],
    "URL": ["https://www.youtube.com/watch\?v\=6c2hT_f5Q2g"],
    "Type": ["video+desc"],
    "Created Date": [""],
    "Download Date": [""],
}

filename = "videos.xlsx"


def start():
    wb = Workbook()

    ws = wb.active
    ws.title = "Video List"
    
    headings = populate_headings()

    ws.append(headings)

    wb.save(filename=filename)