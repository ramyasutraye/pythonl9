k=int(input())
l=[int(x) for x in input().split()]
for i in range(0,k):
    a=l[i]
    while(a==i):
        print(a,end=' ')
        i+=1
else:
    print('-1')
