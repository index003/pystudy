import xlrd
import xlwt

# 利用xlrd和xlwt进行excel读写（xlwt不支持xlsx）

book = xlrd.open_workbook('data_xlrd.xls')
sheet1 = book.sheets()[0]

nrows = sheet1.nrows
print(nrows)

ncols = sheet1.ncols
print(ncols)

row3_values = sheet1.row_values(2)
print(row3_values)

col3_values = sheet1.col_values(2)
print(col3_values)

cell_3_3 = sheet1.cell(2, 2).value
print(cell_3_3)

work_book = xlwt.Workbook()
work_sheet = work_book.add_sheet('test')
work_sheet.write(0, 0, 'A1data')
work_book.save('excel_write.xls')

