n,k=input().split()
n,k=int(n),int(k)
print(n)
print(k)
for i in range (n,k):
	if i>n and i<k:
		if i%2==0:
			print(i,end=' ')
