class Node:
  def __init__(self,value,next=None):
         self.value=value
         self.next=next
# obj=Node(20)
# obj2=Node(30)
# obj.next=obj2
# temp=obj
# obj3=Node(40)
# obj2.next=obj3
# while (temp is not None):
#     print(temp.value)
#     temp=temp.next
class single:
    def __init__(self):
        self.head=None
    def add(self,value):
        obj=Node(value)
        temp=self.head
        if (self.head is None):
            self.head=obj
        else:
            while (temp.next is not None):
                temp=temp.next
            temp.next=obj    
    def display(self):
        temp=self.head
        while (temp is not None):
            print(temp.value)
            temp=temp.next



        
        

        

    
