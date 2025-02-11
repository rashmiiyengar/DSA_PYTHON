def armstrongNumber(num):
    #Convert the number to a string to easily iterate over each digit.
    num_str=str(num)
    len_str=len(num_str)
    
    total= sum(int(digit) ** len_str for digit in num_str)
    
    if total == num:
        print(f"{num} is armstrongNumber number")
    else:
        print(f"{num} is not an armstrong number")

num=153
armstrongNumber(num)