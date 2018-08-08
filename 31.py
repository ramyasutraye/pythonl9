a=[str(x) for x in input()]
b=len(a)
#print(b)
count=0
for i in range(0,b):
    if (a[i].isalpha()):
        count+=1
print(count)
