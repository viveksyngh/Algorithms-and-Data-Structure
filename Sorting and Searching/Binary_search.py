def binary_search(item_list, item) :
    """
    Iterative binary search

    """
    first = 0
    last = len(item_list)
    found = False

    while first <= last and not found :
        mid = (first + last) // 2
        if item_list[mid] == item :
            found = True
        elif item < item_list[mid] :
            last = mid - 1
        else :
            first = mid + 1
    return found

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))
