import openpyxl
wb = openpyxl.load_workbook('score.xlsx')
sheet = wb['kaikeba']
A1_value = sheet['A1'].value
print(A1_value)
wb.close()