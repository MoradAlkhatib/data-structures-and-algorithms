
def quick_sort(arr , left , right):  
    """[sort array by use quick sort algorithm]

    Args:
        arr ([list]): [array how want to sort it]
        left ([int]): [index of first item in the array]
        right ([int]): [index of last item in the array]
    """
    if left < right :  
        postion = partition(arr, left, right)  
        
        quick_sort(arr , left , postion - 1) 
        quick_sort(arr , postion + 1 , right) 
        
    return arr

def partition(arr, left, right):
    """[this function is tack an array and return the postion of item after make it in the correct place inside array as sorted array]

    Args:
        arr ([list]): [array how want to sort it]
        left ([int]): [index of first item in the array]
        right ([int]): [index of last item in the array]

    Returns:
        [int]: [index of item]
    """
    pivot = arr[right] 
    low = left - 1
    for i in range(left,right):
        if arr[i] <= pivot: 
            low += 1              
            swap(arr , i , low) 
    swap(arr, right, low + 1) 
    return low + 1  

def swap(arr, i, low):
    """[make a swap between two items inside an array]

    Args:
        arr ([list]): [array how want to swap inside it]
        left ([int]): [index of first item]
        right ([int]): [index of second item]
    """
    (arr[i] ,arr[low]) = (arr[low] ,arr[i]) 


arr = [8,4,23,42,10,15]
print(arr)
print(quick_sort(arr,0,5))
