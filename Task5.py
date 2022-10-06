def fibonacci_list(k):
    list = [0, 1]
    for i in range (1, k):
        list.append(list[i] + list[i - 1])
    for i in range (k):
        list.insert(0, list[1] - list[0])
    return list

print("Введите количество чисел k")
k = int(input())
print(fibonacci_list(k))