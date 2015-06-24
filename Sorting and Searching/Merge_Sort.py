def merge_sort(A):
	"""
	Divide the array in two half and 
	calls merge_sort on first half and then second half.
	then merge two sorted array in a single aaray and return it

	"""
    n = len(A)
    if n==1 :
        return A
    mid = n//2
    L = merge_sort(A[:mid])
    R = merge_sort(A[mid:])
    return merge(L, R)

def merge(L, R):
	"""
	merge two sorted array L and R 
	in single array and returns it.

	"""
	i=0
	j=0
	A = []
	while i < len(L) and j < len(R) :
		if L[i] < R[j]:
			A.append(L[i])
			i = i+1
		else :
			A.append(R[j])
			j = j+1
	if i < len(L) :
		A.extend(L[i:])
	if j < len(R) :
		A.extend(R[j:])
	return A
a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(merge_sort(a))


