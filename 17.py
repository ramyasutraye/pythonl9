n=int(input())
o=len(str(n))
sum=0
tem=n
while tem>0:
    dig=tem%10
    sum+=dig**o
    tem//=10
if (n==sum):
    print("yes")
else:
    print("no")
