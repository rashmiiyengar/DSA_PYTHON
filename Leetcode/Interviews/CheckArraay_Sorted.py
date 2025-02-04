def check_if_array_is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

print(check_if_array_is_sorted([1,2,2,3,4]))