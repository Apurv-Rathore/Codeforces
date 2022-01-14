import sys,os,io
import math 
from collections import defaultdict
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = lambda: sys.stdin.readline().rstrip("\r\n")

    
def solve():
    n = ii()
    s = list(input())    
    if sorted(s)==s:
        print(0)
        return
    cnt = 0
    res = []
    while 1:
        last = -1 
        p = [0]*n 
        for i in range(n-1,-1,-1):
            xx = 0
            if s[i]=='0':
                xx = 1
            if i==n-1:
                p[i]=xx
            else:
                p[i]+=p[i+1]+xx
        # print(p)  
        
        q = 0
        for i in range(1,n):
            if s[i-1]=='1' and s[i]=="0":
                q = 1 
        if q==0:
            break
        a = []
        one = 0

        for i in range(n):
            if s[i]=='1':
                if one+1<=p[i]:
                    one+=1 
                    a.append(i+1)
                else:
                    break 
        q = []
        for i in range(n-1,-1,-1):
            if s[i]=='0':
                if one>0:
                    q.append(i+1)
                    one-=1
                else:
                    break
        # print(s)
        # print(a)
        q.reverse()
        a.extend(q)
        res.append(a[:])
        i = 0
        j = len(a)-1
        while i<=j:
            s[a[i]-1],s[a[j]-1]=s[a[j]-1],s[a[i]-1]
            i+=1
            j-=1 
        
    print(len(res))
    for i in res:
        print(len(i),*i)

t = 1
t = ii()
for _ in range(t):
    solve()
