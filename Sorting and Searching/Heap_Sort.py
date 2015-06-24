def max_heapify(items, i , size) :
    """
    A -> Array of element
    heapsize -> size of the heap
    i -> index 

    Place the element at index i at correct postion in heap
    """
    left = 2 * i + 1 #left child
    right = 2 * i + 2 #right child
    #size = len(items) - 1
    if left <= size and items[left] > items[i] :
        highest = left
    else :
        highest = i
    if right <= size and items[right] > items[highest] :
        highest = right
    if highest != i :
        items[highest] , items[i] = items[i] , items[highest] # exhcange element at i with largest element 
        max_heapify(items, highest, size)

def build_max_heap(items) :
    """
     A -> An Array
    takes and Array and build a max heap and returns it

    """
    size = len(items)
    for i in range(0 , size // 2) :
        max_heapify(items, i, len(items)-1)

def heap_sort(items) :
    build_max_heap(items)
    print(items)
    size = len(items) - 1
    for i in range(0, len(items)-1) :
        items[size - i] , items[0] = items[0], items[size - i]
        max_heapify( items, 0, len(items[0 : size - i])-1)
        
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
heap_sort(a_list)
print(a_list)


        
        
    
