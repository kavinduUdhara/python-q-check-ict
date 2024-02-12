def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j+1] = arr[j]
                arr[j] = arr[j+1]



    print(arr)

arr = "1 8 5 2 9 4".split()
bubble_sort(arr);