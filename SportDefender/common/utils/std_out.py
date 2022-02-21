# 处理sql查询的结果，放到列表中
import decimal


# 将sql结果转换为列表
def format_sql_result(sql_results, element_poses):
    final_result = []
    if len(element_poses) == 1:
        for sql_result in sql_results:
            element = sql_result[element_poses[0]]
            final_result.append(element)
    elif len(element_poses) > 1:
        for sql_result in sql_results:
            elements = []
            for element_pos in element_poses:
                element = sql_result[element_pos]
                elements.append(element)
            final_result.append(elements)
    else:
        print("Wrong")
    return final_result


# 将decimal.Decimal数据类型的值，转换为字符
def format_decimal(sql_result):
    rep = []
    for row in sql_result:
        if type(row) is list:
            list_x = []
            for data in row:
                if data is None:
                    list_x.append(' ')
                elif type(data) is decimal.Decimal:
                    list_x.append(float(str(data.quantize(decimal.Decimal('0.000')))))
                else:
                    list_x.append(data)
            rep.append(list_x)
        else:
            rep.append(float(str(row.quantize(decimal.Decimal('0.000')))))
    return rep


# 指定浮点数保留的小数点位数，默认为小数点后12位
def format_float(float_num, length=12):
    format_num = str(float_num).split('.')[0] + '.' + str(float_num).split('.')[1][:length]
    return float(format_num)


# 格式化输出
def format_output(some_list):
    for i in range(len(some_list)):
        print(some_list[i], end=' | ')
        if(i+1) % 10 == 0:
            print("\n")
    print("\n")
    print("=====================================")