def linearSearch(nums,num):
    for i in range(len(nums)):
        if nums[i]==num:
            return i
    return -1

num=9
ele=linearSearch([3,2,8,1,9,5],num)
print(f"number {num} is at {ele}th index")