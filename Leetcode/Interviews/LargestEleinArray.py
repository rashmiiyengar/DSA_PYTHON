

# brute force 
# sort all elements and return arr[n-1]
# time o(n log n)
# s(1)

#optimal

# def largestElement(arr):
#     largest=arr[0]
#     for i in range(len(arr)):
#         if arr[i]>largest:
#             largest=arr[i]
            
#     return largest

# arr=[3,2,1,5,2]
# print(largestElement(arr))

def largestEle(arr):
    largest=arr[0]
    for num in arr:
        if num>largest:
            largest=num
    return largest


ele=largestEle([3,2,8,1,9,5])
print(ele)


