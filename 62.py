n=input()
count=0
for i in range (0,len(n)):
    if n[i]=="0" or n[i]=="1":
        count+=1
if count==len(n):
    print("yes")
else:
    print("no")
