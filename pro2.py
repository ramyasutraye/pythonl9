n,k=map(int,input().split())
o=list(str(n))
temp=k
while temp>0:
    temp=temp-1
    del(o[temp])
print("".join(o))
