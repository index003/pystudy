import xlrd

book = xlrd.open_workbook('name_data.xls')
sheet1 = book.sheets()[0]
std_name_list = sheet1.col_values(0)
sky_name_list = sheet1.col_values(1)
hupu_name_list = sheet1.col_values(2)
espn_name_list = sheet1.col_values(3)
print(std_name_list)
print(sky_name_list)
print(hupu_name_list)
print(espn_name_list)


for i in range(1, len(std_name_list)):
    std_name = std_name_list[i]
    sky_name = sky_name_list[i]
    print(std_name)
    print(sky_name)