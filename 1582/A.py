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
    a,b,c = li()
    x = a + 2*b + 3*c 
    print(x%2)

t = 1
t = ii()
for _ in range(t):
    solve()


# 1a  
# 2b 
# 3c 