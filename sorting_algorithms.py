from venv import create
import visualization
def bubble_sort(arr):
    n = len(arr) #gets the length of the given array
    for i in range(n-1):#n works but thats one extra loop!
        for j in range(0,n-i-1):
            #swap if the element found is greater than the original given element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def selection_sort(arr):
    for i in range(len(arr) - 1):
        #find the minimum value of the already sorted elements
        min_index = i
        #j loops through th remaining elements
        for j in range(i+1, len(arr) - 1):
            if arr[j] < arr[min_index]:
                min_index = j
                #constantly makes sure the min index is updated
        #swap them when done
        arr[i], arr[min_index] = arr[min_index],arr[i]
def insertion_sort(arr):
    #start at 1 since the first term is not "moved"
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        #have the key as a constant for the time being
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            #shift all of them over one
        arr[j+1] = key
def quicksort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        pivot = arr[0]
        i = 0
        for j in range(len(arr)-1):
            if arr[j+1] < pivot:
                arr[j+1],arr[i+1] = arr[i+1], arr[j+1]
                i += 1
        arr[0],arr[i] = arr[i],arr[0]
        first_part = quicksort(arr[:i])
        second_part = quicksort(arr[i+1:])
        first_part.append(arr[i])
        return first_part + second_part
def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c
def mergesort(arr):
    """ Function to sort an array using merge sort algorithm """
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        middle = len(arr)/2
        a = mergesort(arr[:middle])
        b = mergesort(arr[middle:])
        return merge(a,b)
def countingSort(arr):
    size = len(arr)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[arr[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(0, size):
        arr[i] = output[i]
def radixsort(arr):
    digit = 1
    atTheEnd = False
    r = 10  # The base of the numbers we choose to sort

    while not atTheEnd:
        # Only remains true if we are calculating for the highest significant digit.
        atTheEnd = True

        # Initialize the bins which are a series of lists
        bins = [list() for _ in range(r)]

        # Place items inside arr buffer into their respective bins
        for i in arr:
            temp = i / digit
            bins[temp % r].append(i)
            if temp > 0:
                atTheEnd = False

        # Put the items in the bins back into the arr buffer
        arrIndex = 0
        for i in range(r): # Goes through each bin
            bin = bins[i]
            for j in bin: # Goes through each element in a given bin
                arr[arrIndex] = j
                arrIndex = arrIndex + 1

        # Increment to sort by the next digit
        digit = digit * r
test_arr = [1,5,7,3,1,4,7,9,42,674,2,4,78]
