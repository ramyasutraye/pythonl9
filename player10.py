n,k=map(str,input().split())
count=0
for i in range (0,len(n)):
    if n[i]==k[i]:
        count+=1
if count==(len(n)-1) or count==(len(n)):
        print("yes")
else:
        print("no")
