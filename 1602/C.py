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
    n = ii()
    a = li()
    if set(a) == set([0]):
        print(*[i for i in range(1,n+1)])
        return
    x = [0]*(len(bin(max(a))) - 2)
    
    for i in range(n):
        b = bin(a[i])[2:][::-1]
        for j in range(len(b)):
            if b[j]=='1':
                x[j]+=1
    g = x[0]
    for i in x:
        g = math.gcd(i,g)
    ans = []
    
    c = sum(x)
    for i in range(1,g):
        if i*i>g:
            break 
        if g%i==0:
            ans.append(i)
            if g//i!=i:
                ans.append(g//i)
    ans.sort()
    real = []
    for i in ans:
        if c%i==0:
            real.append(i)
    if 1 not in real:
        real = [1] + real
    print(*real)

    


    

t = 1
t = ii()
for _ in range(t):
    solve()
