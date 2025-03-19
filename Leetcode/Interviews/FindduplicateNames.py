import re;

#Write a program to validate usernames (alphanumeric, no spaces/special characters, no duplicates).
def isValidUserName(name):
    
    existingusername=set()
    
    if not re.fullmatch(r'[a-zA-Z0-9]+$',name):
        print(f"{name} is not alphanumerix")
        return False
    
    lowerusername=name.lower()
    if lowerusername in existingusername:
        print(f"{lowerusername} already exists")
        return False
    
    existingusername.add(lowerusername)
    print(f"{lowerusername} added successfully")
    return True
usernames = ["User123", "Test_456", "validUser", "user123", "admin!", "hello world"]


for name in usernames:
    isValidUserName(name)