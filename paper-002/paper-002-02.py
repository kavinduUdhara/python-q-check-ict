def func1(num1=10, num2=5):
    return num1 + num2
def func2(num2, num3=3):
    return func1(num2=1) + num3
result = func2(2)
print(result)