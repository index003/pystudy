
# betit = 7176892931
# numbers = range(168)

# for i in numbers:
#     betit = betit - 1
#     print(betit)

# 当前最小id
min_id = 7176892952
# 需要生成的id数量
new_id_count = 40
for new_id in range(min_id - new_id_count, min_id):
    print(new_id)