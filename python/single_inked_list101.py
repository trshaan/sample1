class node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
class Single:
    def __init__(self):
        self.head=None #declares a new list
    def add(self,value): #self sirf head deta hai
        new_node=node(value)
        if (self.head is None):
            self.head=new_node #makes one fresh node holding that value
        else:
            temp=self.head
            while (temp.next is not None):
                temp=temp.next
            temp.next=new_node 
obj=Single()
obj.add(10)
obj.add(9)
obj.add(12)  
temp=obj.head
while temp is not None:
    print(temp.value)
    temp=temp.next

                




    

