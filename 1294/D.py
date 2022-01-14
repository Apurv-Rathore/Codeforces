import heapq
from collections import defaultdict
# t = int(input())
from sys import stdin
t = 1
for _ in range(t):
    # n,k = [int(x) for x in input().split()]
    n,k = list(map(int,stdin.readline().split()))
    dic = defaultdict(lambda:0)
    dic1 = defaultdict(lambda:0)
    h = [0]
    
    heapq.heapify(h)
    for i in range(n):
        x = int(stdin.readline())
        m = (dic[x%k])*k  + x%k
        # print('m,dic[x%k],x%k',m,dic[x%k],x%k,x,k)
        dic[x%k]+=1
        dic1[m]=1
        popped = heapq.heappop(h)
        if (m==popped):
            heapq.heappush(h,m+1)
            while(dic1[popped]==1):
                popped = heapq.heappop(h)
            print(popped)
            heapq.heappush(h,popped)
        elif m>popped:
            heapq.heappush(h,m+1)
            while(dic1[popped]==1):
                popped = heapq.heappop(h)
            print(popped)
            heapq.heappush(h,popped)
        else:
            heapq.heappush(h,m+1)
            while(dic1[popped]==1):
                popped = heapq.heappop(h)
            print(popped)
            heapq.heappush(h,popped)
        # print(h)
        
        
        
        