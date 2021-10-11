import math


def insertShiftArray(arr, s):
    x = math.ceil((len(arr))/2)
    r = arr[-1]
    for i in range(x, len(arr)):
        m = arr[i]
        arr[i] = s
        s = m
    arr += [r]
    
    return arr
