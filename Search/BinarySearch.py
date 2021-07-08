def iterative_binary_search(item, list) :
    low = 0 
    high = len(list) - 1

    while( low <= high ) :

        mid = ( low + high ) // 2
        guess = list[mid]

        if ( item == guess ) :
            return mid

        elif ( item > guess ) :
            low = mid + 1
        
        else :
            high = mid -1

    return -1

list = [1, 2, 4, 8, 10, 20]
item = 4

result = iterative_binary_search(item ,list)

if result != -1:
    print ("Item is found in the list at location", str(result))
else :
    print ("Item not found")

def recursive_binary_search(item, list, low, high): 

    if high >= low :
        mid = (high + low) // 2

        if list[mid] == item:
            return mid

        elif list[mid] > item:
            return recursive_binary_search(item, list, low, mid - 1)

        else :
            return recursive_binary_search(item, list, mid +1 , high)

    else :
        return -1

list = [1, 2, 4, 8, 10, 20]
item = 10

result = recursive_binary_search(item ,list, 0, len(list)-1)

if result != -1:
    print ("Item is found in the list at location", str(result))
else :
    print ("Item not found")