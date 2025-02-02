import sys
def secondSmallestEle(arr):
    smallest=arr[0]
    second_smallest=sys.maxsize-1

    if len(arr)<2:
        return None

    for num in arr:
        if num< smallest:
            second_smallest=smallest
            smallest=num
        if num > smallest and num <second_smallest:
            second_smallest=num

    return second_smallest


ele=secondSmallestEle([3,2,8,1,9,5])
print(ele)