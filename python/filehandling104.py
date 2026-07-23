l=[]
try:
    with open("file.txt","r") as f:
        for i in f:
            l.append(i.strip().split(","))
            
except FileNotFoundError:
    print("error occured")

while True:
    print("enter 1 for adding the task to the list and it status")
    print("enter 2 for viewing all tasks")
    print("enter 3 for marking a task done")
    print("enter 4 for quiting from the program")
    k=int(input("enter your choice: "))
    if (k==1):
        str1=str(input("enter the task"))
        status=str(input("enter the status of the task (done/pending)"))
        z=[str1,status]
        l.append(z)
    elif (k==2):
        for i in l:
            print(i)
    elif (k==3):
        h=0
        for i in l:
            print (i[0]," : ",h)
            h+=1
        c=int(input("enter the number you want to change the status of the task: "))
        l[c][1]="done"

    elif (k==4):
        with open("file.txt","w") as f:
            for i in l:
                f.write(f"{i[0]},{i[1]}\n")
        break
    else:
        print("invalid input")            

