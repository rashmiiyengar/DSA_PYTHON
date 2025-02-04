#rotate the array by one place
# if given array is [1,2,3,4,5,6]
# rotate it to [2,3,4,5,6,1]

import sys
def left_rotate_array_by_one_place(arr):
    if not arr:
        return None
    temp=arr[0]

    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    
    arr[-1]=temp
    return arr

print(left_rotate_array_by_one_place([1,2,3,4,5]))
