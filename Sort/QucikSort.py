def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		part = partition(arr, low, high)
		quickSort(arr, low, part-1)
		quickSort(arr, part+1, high)

def partition(arr, low, high):
	i = (low-1)		 
	pivot = arr[high]

	for j in range(low, high):

		if arr[j] <= pivot:
	
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)


arr = [44, 23, 1, 5, 12]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
print(arr)