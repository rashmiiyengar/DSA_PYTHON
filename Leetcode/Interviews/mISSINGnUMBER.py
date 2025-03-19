nums=[1,2,3,4,6]

n=len(nums)+1

sum_all=n*(n+1)//2
print(sum_all)

print(sum_all-sum(nums))