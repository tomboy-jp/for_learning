import xlwings as xw

wb = xw.Workbook()
xw.Range('A1').value = 'Foo 1'
xw.Range('A1').value
# u'Foo 1'

xw.Range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
xw.Range('A1').table.value
# [[u'Foo 1', u'Foo 2', u'Foo 3'], [10.0, 20.0, 30.0]]

xw.Sheet(1).name
# u'Sheet1'
