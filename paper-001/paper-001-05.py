txt = "this is just a text... saying hello world!"
for i in txt:
    if i in ["a", "e", "i", "o", "u"]:
        continue
    elif i == ".":
        break
    print(i,end="")