lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4, 5, 6]
lst1.append(lst2[3:])
lst1.pop(lst1.index(3))
print(lst1)