k=int(input())
l=[int(x) for x in input().split()]
r=sorted(l)
r.reverse()
for i in range(0,k):
    print(r[i],end='')
