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

def ff(a,new):
    ones = []
    zero = []
    res = 0
    for i in range(len(a)):
        if a[i]==new[i]:
            continue
        if a[i]%2==1:
            ones.append(i)
        else:
            zero.append(i)
    x = len(ones)
    for i in range(x):
        y = ones[i]-zero[i]
        if y<0:
            y*=(-1)
        res += y 
    return res 


def funodd(n,a):
    o = a.count(1)
    e = a.count(0)
    f = 0
    if o>e:
        f = 1 
    new = []
    for i in range(n):
        new.append(f)
        f = abs(1-f)
    ones = []
    zero = []
    res = 0
    for i in range(len(a)):
        if a[i]==new[i]:
            continue
        if a[i]%2==1:
            ones.append(i)
        else:
            zero.append(i)
    x = len(ones)
    for i in range(x):
        y = ones[i]-zero[i]
        if y<0:
            y*=(-1)
        res += y 
    print(res)
    
def funeven(n,a):
    new1 = []
    f = 0
    for i in range(n):
        new1.append(f)
        f = abs(1-f)
    ans = ff(a,new1)
    new2 = []
    f = 1
    for i in range(n):
        new2.append(f)
        f = abs(1-f)
    ans = min(ans,  ff(a,new2))
    print(ans)


def fun(a,n):
    if n%2==1:
        funodd(n,a)
    else:
        funeven(n,a)


def ceil(n):
    x = n//2 
    if n%2:
        x+=1 
    return x 
def solve():
    n = ii()
    a = li()
    o = 0
    e = 0
    for i in range(n):
        a[i]%=2
        if a[i]:
            o+=1
        else:
            e+=1
    if max(o,e)>ceil(n):
        print(-1)
        return 
    fun(a,n)
    

    


t = 1
t = ii()
for _ in range(t):
    solve()
