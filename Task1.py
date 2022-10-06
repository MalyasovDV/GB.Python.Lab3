def sum_odd_positions(list):
    sum = 0
    for i in range(1,len(list), 2):
        sum += list[i]
    return sum

list = [2, 5, 9, 4, 3]
print("Сумма: ", sum_odd_positions(list))