def find_last_index(a, sym):
    # go right until other symbol is found
    i = 1
    while a[i] == sym and i < len(a):
        i *= 2
    othersym = a[i]

    # perform binary search in range
    low = i / 2
    high = i if i < len(a) else len(a) - 1
    mid = None
    while low < high:
        mid = low + (high - low)/2
        if a[mid] == othersym:
            high = mid - 1
        else:
            low = mid + 1

    if a[mid] != sym:
        mid -= 1
    return mid

def locate_last_index(a, sym):
    print "Array:", a
    idx = find_last_index(a, sym)
    print "Last index of ",sym," is ",idx


l = ['a' for i in range(5)]
l.extend(['b' for i in range(15)])
locate_last_index(l, 'a')

l = ['a' for i in range(10)]
l.extend(['b' for i in range(25)])
locate_last_index(l, 'a')

l = ['a' for i in range(16)]
l.extend(['b' for i in range(8)])
locate_last_index(l, 'a')

l = ['a' for i in range(5)]
l.extend(['b' for i in range(5)])
locate_last_index(l, 'a')
