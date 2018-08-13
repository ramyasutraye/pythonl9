a=input.split()
x=list(set(a[0]))
y=list(set(a[1]))
if (len(x)==len(y)):
    print("yes")
else:
    print("no")
