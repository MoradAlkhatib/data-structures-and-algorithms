
def reverseArray(arr):
    # this function tack an array as input

   x=len(arr)
    # iteration over an array revers
   for i  in range(int(x/2)):  
        n = arr[i]
        arr[i] = arr[x-i-1]
        arr[x-i-1] = n
    # and return the same array after revers it  
   return arr
print(reverseArray([1,2,3,4,5,9,8]))