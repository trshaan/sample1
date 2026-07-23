def add(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
while True:
    while True:
        try:
            num1=int(input("enter the 1st number"))
            num2=int(input("enter the 2nd number"))
            break
        except ValueError:
            print("exception occured")
    print("enter 1 for addition")
    print("enter 2 for subtraction")
    print("enter 3 for mutlipcation")
    print("enter 4 for division")
    while True:
        try:
            p=int(input("enter your choice: "))
            if (p==1):
                print(add(num1,num2))
            elif(p==2):
                print(subtraction(num1, num2))
            elif (p==3):
                print(multiplication(num1, num2))
            elif(p==4):
                try:
                    print(division(num1, num2))
                except ZeroDivisionError:
                    print("zero division error occured")
            else:
                print("inavlid input")
        except ValueError:
            print("enter a number")
                                        



