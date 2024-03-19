total = 0
count = 0
marks = [10, -20, 60, 50, 100, 101, 60]
for mark in marks:
    if mark < 0:
        continue
    elif mark > 100:
        break
    else:
        count += 1
        total += mark
#print the avg. of marks
print(total / count)
print(count)