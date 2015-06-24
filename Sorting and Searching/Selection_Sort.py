def selection_sort( items ) :
	"""
	selection sort sorts an array of element by 
	selecting maximum value from usorted part and 
	adding it to start of the sorted part in each step.

	sorted part --- > starts from the end of the array
	usorted part ---> starts from the begining of the array

	"""
    size = len(items)
    for i in range(0 , size - 1 ) : # Number of iterations = 1 less than size
        max_index = 0
        for j in range( 1, size - i ) :
            if items[ max_index ] < items [ j ] : # find index of the largest element in unsorted part
                max_index = j
        items[max_index] , items[ j ] = items[ j  ] , items[ max_index ] # swaps with the last element in unsorted part 

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)
             
