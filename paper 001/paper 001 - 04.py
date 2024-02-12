x = [1, 2, 3, 4, 5, 6]
y = x
z = x.copy()
x.clear()
x.append(7)
z.insert(3,5)
print(len(x))
print(y)
print(z)
