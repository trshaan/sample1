n=int(input("enter a number: "))
p=n//2
q=True
for i in range(2,p+1):
    if n%i==0:
        q=False
if (q):
    print("prime number")
else:
    print("not a prime number")           