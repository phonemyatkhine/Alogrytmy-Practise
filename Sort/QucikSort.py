def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        part = partition(arr, low, high)
        quickSort(arr, low, part-1)
        quickSort(arr, part+1, high)

def partition(arr, low, high):
    i = (low-1)		 #i for iterating the array
    pivot = arr[high] #set pivot at highest index
    print("for low ",low ,"high ", high)
    for j in range(low, high): #starts from 0 to arr len
        
        if arr[j] <= pivot: #checks if pivot is bigger than index starting from 0
	
            i = i+1 #iterations if pivot is bigger
            arr[i], arr[j] = arr[j], arr[i] #swap
        print(arr)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


arr = [11,23,8,1,9]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
print(arr)