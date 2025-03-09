#def reverseNum(num):
 #   return int(str(num)[::-1])

def reverseNum(num):
    revNum=0
    while num>0:
        last=num%10
        revNum=revNum *10 +last
        num//=10
    return revNum
    
print(reverseNum(6789))