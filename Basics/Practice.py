str="hello world"

def reverse_str_preservingwhitespace(str):
    chars=[char for char in str if char!=" "]
    chars.reverse()
    print(chars)

    result=list(str)
    char_index=0

    for i in range(len(result)):
        if result[i]!= " ":
            result[i]=chars[char_index]
            char_index+=1
    return "".join(result)

print(reverse_str_preservingwhitespace(str))
