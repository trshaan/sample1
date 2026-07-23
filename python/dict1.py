
class Student:
    def __init__(self, name, marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def calcaverage(self):
        avg=(self.marks1+self.marks2+self.marks3)/3
        print("average marks of the student is ",avg)    
l=[]
while True:
    print("enter 1 for adding a student")        
    print("enter 2 for viewing all students")
    print("enter 3 for viewing the topper")
    print("enter 4 for quiting from the program")
    m=int(input("enter you choice: "))
    if (m==4):
        break
    elif (m==1):
        name=input("enter your name")
        marks1=int(input("enter your marks for the 1st subject"))
        marks2=int(input("enter your marks for the 2nd subject"))
        marks3=int(input("enter the marks for the third subject"))
        s1=Student(name, marks1, marks2, marks3)
        s1.calcaverage()
        l.append(s1)
    elif (m==2):
        for i in l:
            print("name : ",i.name)
            print("marks for the 1st subject: ",i.marks1)
            print("marks for the 2nd subject: ",i.marks2)
            print("marks for the 3rd subject: ",i.marks3)
            i.calcaverage()