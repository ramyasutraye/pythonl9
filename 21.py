n,a,d=map(int,input().split())
z=0
for i in range(0,n+1):
    z=z+(a+(i-1)*d)
print(z)
