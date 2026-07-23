class contact:
    def __init__(self, name, phone, email):
        self.name=name
        self.phone=phone
        self.email=email
    def display(self):
        print("the name of the contact is ",self.name)    
        print("the phone number of the contact is ",self.phone)
        print("the email adress of the contact is ",self.email)  
l=[]
try:
    with open("lines.txt","r") as f:
        for i in f:
            u=(i.strip().split(","))
            parts=contact(u[0],u[1],u[2])
            l.append(parts)
except FileNotFoundError:
    print("file not found error")            


while True:
    print("enter 1 for adding a contact")
    print("enter 2 for viewing all contacts")
    print("enter 3 for searching for the contact")
    print("enter 4 for quitting from the program")
    t=int(input("enter your choice: "))
    if (t==1):
        nm=input("enter the name of the contact")
        phno=input("enter the phone no of the contact")
        eml=input("enter the email adress of the contact")
        s1=contact(nm,phno,eml)
        l.append(s1)
    elif(t==2):
        for i in l:
            i.display()


    elif(t==4):
        with open("lines.txt","w") as f:
            for i in l:
                f.write(f"{i.name},{i.phone},{i.email}\n")
        break  
    elif (t==3):
        nmsea=str(input("enter the name you want to serch: "))
        n=False
        for i in l:
            if nmsea==i.name:
                i.display()
                n=True
        if (not n):
            print("cotact not found")
                    

 

