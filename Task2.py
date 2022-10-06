def list_of_multiplicated_pairs(list):
    resultlist = []
    n = len(list)
    if (n % 2 == 0):
        for i in range(0,n//2):
            resultlist.append(list[i]*list[n-i-1])
    else:
        for i in range(0,n//2 + 1):
            resultlist.append(list[i]*list[n-i-1])
    return resultlist

list1 = [ 2, 3, 4, 5, 6 ]
print(list1, "->", list_of_multiplicated_pairs(list1))
list2 = [ 2, 3, 5, 6 ]
print(list2, "->", list_of_multiplicated_pairs(list2))