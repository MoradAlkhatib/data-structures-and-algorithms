def mergesort(arr):
    """[tack an array as an argument then sort it]

    Args:
        arr ([list]): [Array ]

    Returns:
        [list]: [use merge function to return array]
    """
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        return Merge( arr ,left, right)

def Merge(arr ,left, right ):
    """[function how merge for the array]

    Args:
        arr ([list]): [array]
        left ([int]): [index of first element of the array]
        right ([int]): [index of last element of the array]

    Returns:
        [type]: [description]
    """
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


if __name__=='__main__':
    print(mergesort([2,5,4,8,9,10]))