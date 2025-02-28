def selectionSort(array, size):
    
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])

arr = [2, 3, 5, 7, 9, 11, 12, 4]
size = len(arr)
selectionSort(arr, size)
print(arr)
