with open('D:\\set_limit.yaml','a',encoding='utf-8') as f:

    for i in range(1361,1626):
        res_index = ' '*6 + '-' + '\n'
        res_le_g = ' '*8 + 'marketFinanceConfigId: ' + str(i) + '\n'
        res_le_o = ' '*8 + 'bettingLimit: 1000' + '\n'

        res = res_index + res_le_g + res_le_o
        f.write(res)

# 输入多个空格
print('q'+' '*3+'q')
