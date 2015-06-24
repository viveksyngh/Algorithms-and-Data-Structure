def bubble_sort( items ) :
    size = len(items)
    for i in range(0,size - 1) :
        for j in range(0, size - i -1) :
            if items[j] > items[j + 1] :
                items[ j ] , items [ j + 1] = items[ j + 1] , items[ j ]


def short_bubble_sort( items ) :
    pass_num = len(items) - 1
    exchanges = True
    while pass_num > 0 and exchanges :
        exchanges = False
        for i in range(0, pass_num) :
            if items [ i ] > items[ i + 1] :
                exchanges = True
                items[ i ] , items [ i + 1] = items[ i + 1], items[ i ]
        pass_num  -=  1
    
a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
short_bubble_sort(a)
print(a)

