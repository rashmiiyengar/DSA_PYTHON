#Remove duplicates in place from a sorted array
#1,2,3,3,4,4,5
#1,2,3,4,5,_,_
#return number of unique elements

def removeDuplicates(arr):
    j=0 # consider j pointer
    for i in range(1,len(arr)):
        if arr[i]!=arr[j]:
            j+=1
            arr[j]=arr[i]
    
    return j+1

print(removeDuplicates([1,1,2,3,3,4,4,4,5]))