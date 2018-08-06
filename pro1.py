import os
k=[]
r=int(input())
for i in range(r):
    a=str(input())
    k.append(a)
print(os.path.commonprefix(k))
    
