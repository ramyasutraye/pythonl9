z=int(input())
c=[int(y) for y in input().split()]
r=sorted(c)
for x in range(z):
    print(r[x],end=' ')
