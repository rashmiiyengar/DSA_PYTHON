# def secondLargestEle(arr):
#     if len(arr)<2:
#         return None #No second largest element possible
#     sr=sorted(arr)

#     largest=sr[-1]
#     for i in range(len(sr)-2,-1,-1):
#         if sr[i]!=largest:
            
#             return sr[i]

#     return None # if all elements are same

# ele=secondLargestEle([3,2,8,1,9,5])
# print(ele)

import sys
def secondLargestEle(arr):
    largest=arr[0]
    second_largest=-sys.maxsize-1

    if len(arr)<2:
        return None

    for num in arr:
        if num> largest:
            second_largest=largest
            largest=num
        if num < largest and num >second_largest:
            second_largest=num

    return second_largest

ele=secondLargestEle([3,2,8,1,9,5])
print(ele)