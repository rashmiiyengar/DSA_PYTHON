class LastWordCount:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        s=s.split(' ')
        return len(s[-1])

str_ = "hello workld"
obj = LastWordCount()
print(obj.lengthOfLastWord(str_))
        