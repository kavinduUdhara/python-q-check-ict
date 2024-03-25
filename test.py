arr = [2,8,5,6,7,9]
len = len(arr)
count = 0

while count < len:
    count2 = 0
    count += 1
    while count2 < len - 1:
        if arr[count2] > arr[count2+1]:
            temp = arr[count2]
            arr[count2] = arr[count2+1]
            arr[count2+1] = temp
        count2 += 1

print(arr)