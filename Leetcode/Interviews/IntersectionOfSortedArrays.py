def intersectionOfSortedArray(arr1,arr2):
    i,j=0,0
    result=[]
    
    while i<len(arr1) and j < len(arr2):
        if arr1[i]==arr2[j]:
            if not result or result[-1]!=arr1[i]:
                result.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
            
    return result
        
arr1=[1,2,3,4,5]
arr2=[2,4]

print(intersectionOfSortedArray(arr1,arr2))