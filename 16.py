n,k=input().split()
n,k=int(n),int(k)
for i in range (n+1,k):
    count=0
    for j in range (1,i):
            if i%j==0:
                count+=1
                if count==2:
                    break
    else:
        print(i,end=' ')
