x=[str(x) for x in input()]
for i in range(0,len(x)):
    if i%2!=0:
        x[i-1],x[i]=x[i],x[i-1]
        print(x[i-1],x[i],sep="",end="")

