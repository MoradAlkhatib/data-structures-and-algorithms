
def binarySearch(arr, n): 
    start = 0
    end = len(arr) - 1             
    mid = 0
  
    while start <= end: 
  
        mid = (end + start) 
  
        # Check if n is present at mid 
        if arr[mid] < n: 
            start = mid + 1
  
        # If n is greater, ignore left half 
        elif arr[mid] > n: 
            end = mid - 1
  
        # If n is smaller, ignore right half 
        else: 
            return mid 
  
    # If we reach here, then the element was not present 
    return -1

            
