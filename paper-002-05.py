lst1 = [5, 8, 7, 3, 2]
lst2 = [4, 2, 6, 8, 7]

def find_equal(arr1, arr2):
    for i in arr1:
        for x in arr2:
            print("*", end="")
            if i == x:
                return i

find_equal(lst1, lst2)