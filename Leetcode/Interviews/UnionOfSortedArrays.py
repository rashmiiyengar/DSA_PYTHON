def union_sorted_arrays(arr1,arr2):
    i,j=0,0
    result=[]

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            if not result or result[-1]!=arr1[i]:
                result.append(arr1[i])
            i+=1
        
        elif arr1[i]>arr2[j]:
            if not result or result[-1]!=arr2[j]:
                result.append(arr2[j])
            j+=1
        else:
            if not result or result[-1]!=arr1[i]:
                result.append(arr1[i])
            i+=1
    
    while i<len(arr1):
        if not result or result[-1]!=arr1[i]:
            result.append(arr1[i])        
        i+=1
    
    while j<len(arr2):
        if not result or result[-1]!=arr2[j]:
            result.append(arr2[j])
        j+=1
         
    return result
        

arr1 = [1, 2, 4, 5, 6, 7]
arr2 = [2, 3, 5, 7]
print(union_sorted_arrays(arr1, arr2))