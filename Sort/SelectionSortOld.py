def findSmallest(arr) :
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)) :
        if ( smallest > arr[i]) :
            smallest = arr[i] 
            smallest_index = i
    return smallest_index

def selectionSort(arr) :
    newArr = []
    for i in range(len(arr)) :
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest)) #arr.pop basically pop outs the index and keep the others
    return newArr

print (selectionSort([10,5,23,12,4,1]))

# def sum(arr) :
#     if(len(arr) == 1) :
#         return 1
#     else :
#         return arr.pop(0) + sum(arr)

# print (sum([10,5,23,12,4,1]))