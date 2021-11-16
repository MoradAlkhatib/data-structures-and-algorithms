
def quick_sort(arr , left , right):   # [8, 4, 23, 42, 16, 15]  0 , 5
    if left < right :   # 0 < 5
        postion = partition(arr, left, right)  # 3 
        print("1") 
        quick_sort(arr , left , postion - 1) # [8, 4, 10, 15, 23, 42]  0 , 2
        print("2")   
        quick_sort(arr , postion + 1 , right) # [8, 4, 10, 15, 23, 42]  4, 5
        # print("3")

def partition(arr, left, right):# [8, 4, 23, 42, 10, 15]  
    pivot = arr[right] # 15
    low = left - 1 # -1 
    for i in range(left,right): #  4  5
        if arr[i] <= pivot: #  10 <= 15
            low += 1               # 2
            swap(arr , i , low) # [8, 4, 23, 42, 10, 15]  4 , 2 [8, 4, 10, 42, 23, 15]
    swap(arr, right, low + 1) # [8, 4, 10, 42, 23, 15] 5 , 3  [8, 4, 10, 15, 23, 42]
    return low + 1  # 3

def swap(arr, i, low):
    (arr[i] ,arr[low]) = (arr[low] ,arr[i]) 
    # temp = arr[i] 
    # arr[i] = arr[low] 
    # arr[low] = temp

arr = [8,4,23,42,10,15]
print(arr)
quick_sort(arr,0,5)
print(arr)

# array = [ 10, 7, 8, 9, 1, 5 ]
# quick_sort(array , 0 , len(array) - 1 )
  
# print(f'Sorted array: {array}')