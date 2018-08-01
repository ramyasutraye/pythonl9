n,k=map(int,raw_input().split())
for i in range (n,k):
	if ((i%2)!=0 and i!=n and i!=k):
		print(i)
		print(' ')
