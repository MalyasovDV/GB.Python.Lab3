def find_difference(list):
    max = list[0] % 1
    min = list[0] % 1
    for i in range(1, len(list)):
        decimalPart = list[i] % 1
        if (decimalPart % 1 > max):
            max = list[i] % 1
        if (decimalPart % 1 < min) and (decimalPart % 1 != 0):
            min = list[i] % 1
    return max - min

list = [1.1, 1.2, 3.1, 5, 10.01]
print("%.2f" % find_difference(list))