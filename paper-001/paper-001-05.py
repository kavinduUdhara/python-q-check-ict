txt = "this is just a text... saying hello world!"
for i in txt:
    if ["a", "e", "i", "o", "u"] in i:
        continue
    elif i == ".":
        break
    print("i",end="")