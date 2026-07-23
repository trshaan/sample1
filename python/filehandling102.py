class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def calcaverage(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print("average marks of the student is ", avg)
        return avg

l = []
try:
    with open("student101.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",") 
                s5=Student(parts[0], int(parts[1]), int(parts[2]), int(parts[3]))
                l.append(s5)
except FileNotFoundError:
    print("'file not exists!!!!!")

while True:
    print("enter 1 for adding a student")
    print("enter 2 for viewing all students")
    print("enter 3 for viewing the topper")
    print("enter 4 for quiting from the program")
    m = int(input("enter your choice: "))
    if (m == 4):
        for i in l:
            with open("student101.txt","w") as f:
                line = f"{i.name},{i.marks1},{i.marks2},{i.marks3}\n"
                f.write(line)

        break
    elif (m == 1):
        name = input("enter the student's name: ")
        marks1 = int(input("enter marks for the 1st subject: "))
        marks2 = int(input("enter marks for the 2nd subject: "))
        marks3 = int(input("enter marks for the 3rd subject: "))
        s1 = Student(name, marks1, marks2, marks3)
        s1.calcaverage()
        l.append(s1)
    elif (m == 2):
        for i in l:
            print("name : ", i.name)
            print("marks for the 1st subject: ", i.marks1)
            print("marks for the 2nd subject: ", i.marks2)
            print("marks for the 3rd subject: ", i.marks3)
            i.calcaverage()
    elif (m==3):
        s101=l[0]
        for i in l:
            if (i.calcaverage()>s101.calcaverage()):
                s101=i
        print(s101.name)
        print(s101.marks1)
        print(s101.marks2)
        print(s101.marks3)   
        s101.calcaverage()     
    else:
        print("inavlid input")

    ## elif (m==3):
    # k=[]
    # for i in l :
    #      k.append(i.calcaverage()) 
    # p=max(k)
    # for i in l:
    #      if(i.calcaverage()==p):
    #            print(i.name)
    #            then it goes onto print all three marks and also prints the average           


