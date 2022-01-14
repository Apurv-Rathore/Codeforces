import sys,os,io
import math 
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
    n,c = input().split()
    n = int(n)
    s = input()
    if list(set(s))==[c]:
        print(0)
        return 
    if s[-1]==c:
        print(1)
        print(n)
        return 
    if list(set(s[:-1]))==[c]:
        print(1)
        print(n-1)
        return
    
    for i in range(n-1,-1,-1):
        if s[i]==c:
            x = i+1
            if 2*x>n:
                print(1)
                print(x)
                return


    print(2)
    print(n,n-1)




     

    

t = 1
t = ii()
for _ in range(t):
    solve()
