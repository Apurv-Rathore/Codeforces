import sys,os,io
import math 
from collections import defaultdict
from collections import deque

def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline



def solve():
    n = ii()
    a = li()
    l = []
    for i in range(n):
        l.append([a[i] , i])
    l.sort(reverse=True)
    anss = [0]*(n+1)
    left = -1
    right = 1 
    now = 1 
    res = [0]
    ans = 0
    for i in range(n):
        # print(l[i])
        if now==1:
            res.append(right)
            ans += 2*abs(right)*l[i][0]
            anss[l[i][1]+1] = right
            right+=1
            now = 0
        else:
            now = 1 
            ans += 2*abs(left)*l[i][0]
            anss[l[i][1]+1] = left
            res.append(left)
            left-=1
    print(ans)
    print(*anss)




        









t = 1
t = ii()
for _ in range(t):
    solve()
