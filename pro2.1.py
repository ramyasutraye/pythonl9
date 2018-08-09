n,k=map(int,input().split())
o=list(str(n))
li=sorted(o)
li.reverse()
temp=0
while temp<k:
    del(li[temp])
    temp+=1
c=li.reverse()
print("".join(li))
