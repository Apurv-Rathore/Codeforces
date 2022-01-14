import heapq
n,k=map(int,input().split())
a=sorted(tuple( list(map(int,input().split())) for  i in range(n)),key= lambda x : x[1],reverse=True)
time=[]
m=0
s=0

for t,b in a:
    s+=t
    heapq.heappush(time,t)
    if len(time)>k:
        s-=heapq.heappop(time)
    m=max(m,s*b)
print(m)    
    