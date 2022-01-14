
import sys,os,io
import math 
import random
from collections import defaultdict
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline



def solve():
    n,k = li()
    s = input()
    d = defaultdict(lambda:0)
    for i in s:
        d[i]+=1 
    l = []
    o = 0
    for i in d:
        if d[i]==1:
            o+=1
        elif d[i]%2==1:
            o+=1
            l.append(d[i]-1)
        else:
            l.append(d[i])
    ans = sum(l)
    # print(l)
    x = 0
    xx = 0
    if ans//k>0:
        xx = sum(l)-k*(ans//k)
        # print(xx,sum(l)-k*(ans//k))
    if o+xx>=k and (ans//k)%2==0:
        x = 1
    
    print(max(1,ans//k+x))
    # 2
    # 2
    # 2
    # 1
    # 1
    # low = 0
    # high = n
    # ans = 0
    # while low<=high:
    #     mid = (low+high)//2
    #     l1 = l[:]
    #     o1 = o

    #     ptr = 0
    #     cur = mid
    #     f = 1
    #     for i in range(k):
    #         if cur==0:
    #             cur = k
    #             continue 
    #         if cur==1 and o1>0:
    #             o1-=1
    #             cur = k 
    #             continue

    #         while ptr<len(l1) and cur>0:
    #             if l1[ptr]>=cur:
    #                 l1[ptr]-=cur 
    #                 break 
    #             else:
    #                 cur -= l1[ptr]
    #                 ptr+=1 
    #         if cur>0:
    #             f = 0
    #             break 
    #         cur = k 
    #     if f==1:
    #         ans = max(ans , mid)
    #         low = mid+1 
    #     else:
    #         high = mid-1
    # print(ans)




        



t = 1
t = ii()
for _ in range(t):
    solve()
