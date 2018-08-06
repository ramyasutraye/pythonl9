a=int(input())
b=[int(y) for y in input().split()]
s=sorted(b)
for x in range(a):
    print(s[x],end=' ')
