s1=str(input("enter a string: "))
p=0
for i in range(len(s1)):
    if s1[i].lower() in 'aeiou':
        p+=1
print("the number of vowels in the string is",p)        