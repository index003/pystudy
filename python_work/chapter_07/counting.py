current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

current_number_new = 0
while current_number_new < 10:
    current_number_new += 1
    if current_number_new % 2 == 0:
        continue
    print(current_number_new)