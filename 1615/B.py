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



bits = [[0 for j in range(20)] for i in range(200001)]
# print(bits)
for i in range(200001):
    for j in range(20):
        if i>0:
            bits[i][j]+=bits[i-1][j]
        if (1<<j)&i!=0:
            bits[i][j]+=1



def solve():
    l,r = li()
    ans = 0
    for i in range(20):
        ans = max(bits[r][i]-bits[l-1][i],ans)
    print(r-l+1-ans)


t = 1
t = ii()
for _ in range(t):
    solve()
