class node:
    def __init__(self, value, next=None, prev=None):
        self.value=value
        self.prev=prev
        self.next=next
class dequeue:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_rear(self, value):
        if self.is_empty():
            obj=node(value)
            self.head=obj
            self.tail=obj
        else:
            # temp=self.head
            # while temp.next is not None:
            #     temp=temp.next
            # obj=node(value)
            # temp.next=obj
            # obj.prev=temp    
            temp=self.tail
            obj=node(value)
            temp.next=obj
            obj.prev=temp
            self.tail=obj
    def add_front(self,value):
        if self.is_empty():
            obj=node(value)
            self.head=obj
            self.tail=obj
        else:
            # temp=self.tail
            # while temp.prev is not None:
            #     temp=temp.prev
            # obj=node(value)
            # obj.next=temp
            # temp.prev=obj
            # self.head=obj            
            temp=self.head
            obj=node(value)
            obj.next=temp
            temp.prev=obj
            self.head=obj
    def display_front(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def display_rear(self):
        temp=self.tail
        while temp is not None:
            print(temp.value)
            temp=temp.prev
    def remove_front(self):
        if self.is_empty():
            return None
        elif self.head is self.tail:
            self.head=None
            self.tail=None
            return self.head.value
        else:
            temp=self.head.value
            self.head=self.head.next
            self.head.prev=None
            return temp
    def remove_rear(self):
        if self.is_empty():
            return None
        elif self.head is self.tail:
            self.head=None
            self.tail=None
            return self.head.value
        else:
            temp=self.tail.value
            self.tail=self.tail.prev
            self.tail.next = None
            return temp
    def is_empty(self):
        return self.head is None
    def peek_front(self):
        if self.is_empty():
            return None
        return self.head.value
    def peek_rear(self):
        if self.is_empty():
            return None
        return self.tail.value
obj=dequeue()              
while True:
    print("enter 1 for adding elements at the end of the list")
    print("enter 2 for adding elements elements at the front of the list")
    print("enter 3 for displaying the list from the front")
    print("enter 4 for displaying elements from the list starating from the back")
    print("enter 5 for peeking into the list from the front")
    print("enter 6 for removing from the front")
    print("enter 7 for removing from the back")
    print("enter 8 for peeking into the list from the back")
    ch=int(input("enter your choice: "))
    if ch==1:
        ele=int(input("enter the element you want to enter in the list"))
        obj.add_rear(ele)
    elif (ch==2):
        ele=int(input("enter the element you want to enter in the list"))
        obj.add_front(ele)
    elif(ch==3):
        obj.display_front()
    elif(ch==4):
        obj.display_rear()
    elif (ch==5):
        print(obj.peek_front())    
    elif (ch==6):
        print(obj.remove_front())
    elif (ch==7):
        print(obj.remove_rear())    
    elif (ch==8):
        print(obj.peek_rear())    
    else:
        print("invalid input")
    pos=input("do you want to continue (y/n) ?")
    if pos=="n":
        break                

        