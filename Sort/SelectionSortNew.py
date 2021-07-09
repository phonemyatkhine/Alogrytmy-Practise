def selectionSort(arr) :
    for i in range(len(arr)) :
        smallest_index = i
        for j in range(len(arr)) :
            if arr[smallest_index] < arr[j] :
                smallest_index = j
            arr[i] , arr[smallest_index] = arr[smallest_index] , arr[i] #swap variables very useful
    return arr

print(selectionSort([10,5,23,12,4,1]))