import openpyxl as px
import numpy as np

wb = px.Workbook()
ws = wb.active

arr = np.arange(10000).reshape(100,100)
for x, r in enumerate(arr):
    for y, val in enumerate(r):
        ws.cell(row=x+1, column=y+1).value = val

wb.save("xlsx/test.xlsx")
