""" Implementation of in place quicksort """

def partition(array, left, right):
    # Choose middle element as pivot.
    pivotIndex = (left+right) >> 1
    pivotValue = array[pivotIndex]

    # move array[right] to array[pivotIndex] position
    # note that we already store array[pivotIndex] in pivotValue
    array[pivotIndex] = array[right]

    # elements <= the pivot are moved to the left (smaller indices)

    # At all times, elements to the left of storeIndex are <= to the pivot
    # It serves as a location that elements <= the pivot can be swapped into.
    storeIndex = left 

    for i in xrange(left, right): # Do not include the last array element.
        temp = array[i]
        if temp <= pivotValue:
            # Swap the items at storeIndex and array[i]
            array[i] = array[storeIndex]
            array[storeIndex] = temp
            storeIndex += 1 # Move the store index right. The element we just swapped into the storeIndex will stay at is position now.

    # At this point, we know the storeIndex points to an element that is greater than the pivot.
    # Move this to the rightmost position, so that it's guaranteed to be right of the pivot.
    # The pivotValue can go in the storeIndex position, since everything left of there is <= pivotValue.
    array[right] = array[storeIndex]
    array[storeIndex] = pivotValue
    return storeIndex

def quicksort(array, left, right):
    if left < right:
        pivotIndex = partition(array, left, right)
        quicksort(array,left,pivotIndex-1)
        quicksort(array,pivotIndex+1,right)