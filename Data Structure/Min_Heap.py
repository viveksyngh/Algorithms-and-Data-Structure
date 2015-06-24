import timeit
from timeit import Timer
#importing timeit module to compare times

def min_heapify(A , heapsize, i) :
    """
    A -> Array of element
    heapsize -> size of the heap
    i -> index 

    Place the element at index i at correct postion in heap
    """
    left = 2 * i + 1 #left child
    right =  2 * i + 2 #right child 
    if left <= heapsize  and A[i] > A[left] :
        smallest = left
    else :
        smallest = i

    if right <= heapsize and A[right] < A[smallest] :
        smallest = right

    if smallest != i :
        A[smallest], A[i] = A[i], A[smallest] # exhcange smallest element at i with smallest element 
        min_heapify(A , heapsize, smallest)
    return A


def build_min_heap(A) :
    """
    A -> An Array
    takes an Array and build a min heap and returns it

    """
    heap_size = len(A) - 1
    for i in range(heap_size//2, -1, -1) : #Takes first half of the array and puts them at correct postion 
        A = min_heapify(A, heap_size, i)   #Because other half of the list are leaf elements
    return A


def extract_min(A, heap_size) :
    """
    Extracts min value from the list and returns it.

    """
    A[heap_size], A[0] = A[0] , A[heap_size]
    A = min_heapify(A, heap_size-1,0)
    return A

def kth_smallest(A, k) :
    """
    returns kth smallest element from the heps  

    """
    A = build_min_heap(A)
    for i in range(1, k+1) :
        if i == k :
            A = extract_min(A, len(A)-i)
            return A[len(A)-k]
        else :
            A = extract_min(A, len(A)-i)
            
A = [8, 9, 5, 4, 7 , 3, 2, 6]
print(kth_smallest(A, 2))

#t1 = Timer("kth_smallest(A, 2)", "from __main__ import A, i , kth_smallest,extract_min, build_min_heap, min_heapify")
for i in range(100000, 1000001, 20000) :
    t1 = Timer("kth_smallest(A, 2)", "from __main__ import A, i , kth_smallest,extract_min, build_min_heap, min_heapify")
    A = list(range(i))
    print(i,  t1.timeit(number = 1))
            
    
