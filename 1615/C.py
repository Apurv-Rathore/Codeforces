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
    n = ii()
    a = list(input())
    b = list(input())
    if a==b:
        print(0)
        return 
    if '1' not in a:
        print(-1)
        return
    c = 0
    same1 = 0
    ulte1 = 0
    for i in range(n):
        if a[i]!=b[i]:
            if a[i]=="1":
                ulte1 += 1 
            c+=1 
        else:
            if a[i]=="1":
                same1 += 1
    ans = 1e9
    same = n-c 
    ulte = c
    # print(ulte,ulte1)
    if same%2==1 and (same//2+1==same1):
        ans = same 
    if ulte%2==0 and ((ulte//2)==ulte1):
        ans = min(ans , ulte)
    if ans==1e9:
        ans = -1
    print(ans)

    

t = 1
t = ii()
for _ in range(t):
    solve()
