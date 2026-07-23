class node:
    def __init__(self, value, next=None, prev=None):
        self.value=value
        self.next=next
        self.prev=prev
class circulardequeu:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_front(self, value):
        if self.head is None:
            obj=node(value)
            self.head=obj
            self.tail=obj
            obj.next=obj
            obj.prev=obj
        else:
            obj=node(value)    
            obj.next=self.head
            obj.prev=self.tail
            self.tail.next=obj
            self.head.prev=obj
            self.head=obj
    def add_rear(self, value):
        if self.head is None:
            obj=node(value)
            self.head=obj
            self.tail=obj
            obj.next=obj
            obj.prev=obj
        else:
            obj=node(value)
            obj.next=self.head
            self.head.prev=obj
            self.tail.next=obj
            obj.prev=self.tail
            self.tail=obj     
    def display(self):
        if self.head is None:
            print("nothing to print here")
        else:
            temp=self.head
            print(temp.value)
            temp=temp.next
            while temp is not self.head:
                print(temp.value)
                temp=temp.next
obj=circulardequeu()
while True:
    print("enter 1 for adding elements in the front")
    print("enter 2 for adding elements in the back")
    print("enter 3 for displaying elements")        
    ch=int(input("enter your choice: "))    
    if ch==1:
        ele=int(input("enter the elements you want to add in the list"))
        obj.add_front(ele)
    elif ch==2:
        le=int(input("enter the elements you want to add in the list"))
        obj.add_rear(le)
    elif(ch==3):
        obj.display()
    else:
        print("invalid input")
    str1=input("do you want to continue? (y/n): ")            
    if str1=="n":
        break

