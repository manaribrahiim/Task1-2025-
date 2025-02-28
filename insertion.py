def insertionsort(arr):
    n = len(arr)
    if n <= 1:
        return 
    for j in range(1,n):
        key = arr[j]
        i = j-1 
        while i >= 0 and arr[i] > key: 
            arr[i+1] = arr[i]
            i -= 1 
        arr[i+1] = key 
arr = [2, 3, 5, 7, 9, 11, 12, 4]
insertionsort(arr)
print(arr)
