def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for i in range(0, len(items) - 1):
        for x in range(0, len(items) - 1 - i):
            if items[x]> items[x + 1]:
                items[x], items[x + 1] = items[x + 1], items[x]
    return(items)

def merge_sort(item):
    if len(item)>1:
        middle = len(item)//2
        left = item[:middle]
        right = item[middle:]

        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                item[k]=left[i]
                i += 1
            else:
                item[k]=right[j]
                j += 1
            k += 1

        while i < len(left):
            item[k]=left[i]
            i += 1
            k += 1

        while j < len(right):
            item[k]=right[j]
            j += 1
            k += 1
    return(item)

def quick_sort(item):
    less = []
    equal = []
    greater = []

    if len(item) > 1:
        split = item[0]
        for x in item:
            if x < split:
                less.append(x)
            elif x == split:
                equal.append(x)
            elif x > split:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return item
