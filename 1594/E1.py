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
k = ii()
ans = 6 
mod = int(1e9)+7 

nodes = pow(2,k)
ans = 6 * pow(4,nodes-2,mod)
ans%=mod
print(ans)