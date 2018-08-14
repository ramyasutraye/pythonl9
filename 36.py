n1=[str(x) for x in input()]
c=0
for i in n1:
    if i.isalpha():
        a=0
    elif i.isdigit():
        a=0
    else:
        c+=1
print(c)
    
