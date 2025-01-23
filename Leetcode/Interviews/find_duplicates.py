def findDuplicates(str):
    char_count={}
    
    for char in str:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
            
    duplicates ={char:count for char,count in char_count.items() if count>1}
    return duplicates

result=findDuplicates("programming")
print(result)