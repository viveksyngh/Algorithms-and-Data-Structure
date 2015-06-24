def binary_search(item_list, item) :
    """
    Recursive binary search 

    """
    list_len = len(item_list)
    mid = list_len // 2
    if list_len == 0 :
        return False
    else :
        if item_list[mid] == item :
            return True
        elif item < item_list[mid] :
            return binary_search(item_list [  : mid] , item)
        else :
            return binary_search(item_list[mid + 1 : ], item)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))
