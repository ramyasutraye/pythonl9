n1,n2=map(int,input().split())
num=[int(x)for x in input().split()]
for i in range(0,n1):
    if num[i]==n2:
        print("yes")
    else:
        print("no")
