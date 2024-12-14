class SinglyNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
    
    def __str__(self):
        return str(self.val)


#The __str__ method in Python is a special method that defines the string 
#representation of an object. It is invoked when you use the str() function or when an object is printed using print().
 
Head = SinglyNode(1)
A= SinglyNode(3)
B=SinglyNode(4)
C=SinglyNode(7)
    
Head.next =A
A.next =B
B.next=C

    
#traverse list and print values
# curr =Head
    
# while curr:
#     print(curr)
#     curr=curr.next
    
#display linked list o(n)

def display(head):
    curr = head
    elements=[]
        
    while curr:
        elements.append(str(curr.val))
        curr=curr.next
    print(' -> '.join(elements))
    display(Head)
    
    
#Search for a node value O(N)
def search(head,val):
    curr=head
    while curr:
        if val == curr.val:
            return True
        curr=curr.next
        
    return False
print(search(Head,3))



    