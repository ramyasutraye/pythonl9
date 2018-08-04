k=input()
l=[int(x) for x in input().split()]
c=0
for i in range(len(l)):
    if (i==l[i]):
        print(i,end=' ')
        c+=1
if(c==0):
    print('-1')
