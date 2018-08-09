n,k=map(int,input().split())
o=list(str(n))
print(o)
li=sorted(o)
li.reverse()
print(li)
temp=0
while temp<k:
    del(li[temp])
    temp+=1
c=li.reverse()
print("".join(li))
