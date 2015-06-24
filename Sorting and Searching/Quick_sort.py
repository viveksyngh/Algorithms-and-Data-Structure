def quick_sort(items) :
    """
    Quick sort sorts an array 'items'
    Worst Case complexity -- > O(n2) 
    Best  Case complexity -- > O(nlogn)

    """
    quick_sort_helper( items, 0, len(items) - 1 )

def quick_sort_helper (items, first, last) :
    """
    items --> array to be sorted 
    first --> index of the first element
    last --> index of the last element

    """
    if first < last :
        split_pos = partition(items, first , last )

        quick_sort_helper (items, first, split_pos - 1)
        quick_sort_helper (items , split_pos + 1, last )

def partition(items , first, last ) :
    """
    function partition 'items' in two half based on pivot element and 
    returns the index of pivot element in the array 'items'

    items --> array to be sorted 
    first --> index of the first element
    last --> index of the last element

    """
    pivot = items[first]
    left = first +1
    right = last
    done = False
    while not done :
        while left <= right and items[left] <=  pivot :
            left = left + 1
        while right >= left and items[right] >= pivot :
            right = right - 1
        if right < left :
            done = True
        else :
            items[left] , items[right] = items[right] , items[left]

    items[right] , items[first] = items[first] , items[right] #Place the pivot element at correct position
    return right

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)
        
    
