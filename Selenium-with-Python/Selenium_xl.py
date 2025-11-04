import openpyxl

path=r"C:\Users\teodo\Desktop\doc-files\coding\codecademy\Page_Visits_Funnel_Project\Page_Visits_Funnel_Project\cart.xlsx"
workbook=openpyxl.load_workbook(path)
# For single sheet
sheet=workbook.active
sheet.max_row=sheet.max_row
col=sheet.max_column

print(rows)
print(col)