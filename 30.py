hour0,time0=map(int,input().split())
hour1,time1=map(int,input().split())
h0=(hour0*60)+time0
t0=(hour1*60)+time1
t1=h0-t0
h1=t1//60
t1%=60
print(h1,t1,sep=" ")
