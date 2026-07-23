l=[]
try:
     with open("file.txt","r") as f:
          for i in f:
               data=i.strip()
               l.append(data)
except FileNotFoundError:
     print("file not found error occured")               
while True:
    print("enter 1 for entering text")
    print("enter 2 for viewing your notes")
    print("enter 3 for quiting from the program")
    k=int(input("enter your choice: "))
    if (k==1):
        st1=str(input("enter your string: "))
        l.append(st1)
    elif(k==2):
        for i in l:
            print(i)
    elif(k==3):
        with open("file.txt","w") as f:
                for i in l:
                     f.write(f"{i}\n")
        break            
