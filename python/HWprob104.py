L=[]
while True:
    n=int(input("enter a number to be added in the list: "))
    L.append(n)
    s1=str(input("do you to continue(y/n): "))
    if (s1=="n"):
        break   
def max(l):
    u=L[0]
    for i in l:
        if u<i:
            u=i
    return u
print("max number is ",max(L))
L.remove(max(L))
print("the second highest number is the list is", max(L))    
