n,k=map(int,input().split())
tem=0
for i in range (n,k+1):
    count=0
    for j in range (1,i):
            if i%j==0:
                count+=1
                if count==2:
                    break
    else:
        tem+=1
print(tem)
