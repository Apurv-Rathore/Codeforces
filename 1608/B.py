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
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def solve():
    n,a,b = li()
    cnt = n - 2 
    if n==2:
        if a==b==0:
            print(1,2)
        else:
            print(-1)
        return 
    if a+b>cnt:
        print(-1)
        return 
    if abs(a-b)>1:
        print(-1)
        return 
    
    if b>=a:#local minimum more 
        ans = [i for i in range(1,n+1)]
        ans.reverse()
        ind = 1
        for i in range(b):
            ans[ind],ans[ind+1]=ans[ind+1],ans[ind]
            ind+=2 
        if b>a:
            x = ans[ind-1]
            y = ans[ind:]
            ans[ind-1:-1]=y 
            ans[-1]=x 
    else:
        ans = [i for i in range(1,n+1)]
        ans.reverse()
        ind = 1
        for i in range(a):
            ans[ind],ans[ind+1]=ans[ind+1],ans[ind]
            ind+=2 
        x = ans[ind-1]
        y = ans[ind:]
        ans[ind-1:-1]=y 
        ans[-1]=x 
        # print(*ans)
        for i in range(n):
            ans[i] = n - ans[i]+1
    print(*ans)

        

            


t = 1
t = ii()
for _ in range(t):
    solve()
