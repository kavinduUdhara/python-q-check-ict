def lucky_num(num = 5):
    return num * 2
def lucky_statement(name = "Joe"):
    num = len(name)
    lu_num = lucky_num()
    return f"Hi {name}, your lucky num is {lu_num}"
print(lucky_statement("Doe"))