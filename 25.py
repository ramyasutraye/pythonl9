a=int(input())
b=[int(y) for y in input().split()]
s=sorted(b)
if a%2==0:
    x=(a-1)//2
    y=x+1
    z=(s[x]+s[y])/2
    print(z)
else:
    x=(a)//2
    print(s[x])
