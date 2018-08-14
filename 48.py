n1=int(input())
n2=[int(x)for x in input().split()]
sum=0
for i in range(0,n1):
    sum+=n2[i]
s=sum//n1
print(s)

