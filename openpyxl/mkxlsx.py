import openpyxl as px
import numpy as np
import os

l = os.listdir()
for i in l:
    if i == "test.xlsx":
        os.remove("test.xlsx")

wb = px.Workbook()
ws = wb.active

arr = np.arange(1,10001).reshape(100,100)
for x, r in enumerate(arr):
    for y, val in enumerate(r):
        ws.cell(row=x+1, column=y+1).value = val

wb.save("test.xlsx")
