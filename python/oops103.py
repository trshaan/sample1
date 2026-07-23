marks1=int(input("enter the marks for the 1st subject"))
marks2=int(input("enter the marks for the 2nd subject"))
marks3=int(input("enter the marks for the 3rd subject"))
class student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def avgmarks(self):
        avg=(self.marks1+self.marks2+self.marks3)/3
        print("the avg marks are ",avg)
s1=student("trish", marks1, marks2, marks3)
s1.avgmarks()


        

