class Student:
    def __init__(self,name,roll_no,marks1,marks2,marks3):
        self.name=name
        self.roll_no=roll_no
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def display(self):
        print("name : ",self.name)
        print("roll no : ",self.roll_no)
        print("marks for the 1st subject : ",self.marks1)
        print("marks for the 2nd subject : ",self.marks2)
        print("marks for the 3rd subject : ",self.marks3)
    def calcaverage(self):
        avg=(self.marks1+self.marks2+self.marks3)/3
        return avg   
l=[] 
try:
    with open("student.txt","r") as f:
        for i in f:
            parts=i.strip().split(",")
            s2=Student(parts[0],parts[1],int(parts[2]),int(parts[3]),int(parts[4]))
            l.append(s2)
except FileNotFoundError:
    print("file not found ")
            
while True:
    print("enter 1 for adding the student")
    print("enter 2 for viewing all students")
    print("enter 3 for searching by roll no")
    print("enter 4 for showing the topper")
    print("enter 5 for for deleting a student")
    print("enter 6 for quitting from the student")
    p=int(input("enter your choice: "))
    if (p==1):
        nm=input('enter your name: ')
        rlno=int(input("enter your roll no: "))
        m1=int(input("enter your marks for the 1st subject: "))
        m2=int(input("enter your marks for the 2nd subject: "))
        m3=int(input("enter your marks for the 3rd subject: "))
        s1=Student(nm,rlno,m1,m2,m3)
        l.append(s1)
    elif (p==2):
        for i in l:
            i.display() 
    elif (p==3):
        roll_no=int(input("enter the roll no you want to search"))
        n=False
        for i in l:
            if i.roll_no==roll_no:
                i.display()
                n=True
        if not n:
            print("contact not found")       
    elif (p==4):
        j=l[0].calcaverage()
        p=0
        for i in l:
            if i.calcaverage()>j:
                j=i.calcaverage()
                p=i
        p.display()        

    elif (p==5):
        roll_no=int(input("enter the roll no whose student u want to delete: "))
        for i in l:
            if i.roll_no==roll_no:
                l.remove(i)
    elif (p==6):
        with open("student.txt","w") as f:
            for i in l:
                lines=f"{i.name},{i.roll_no},{i.marks1},{i.marks2},{i.marks3}\n"
                f.write(lines)
            break    
    else:
        print("invalid input")                










