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
    s = list(input())
    l = [[-1 for i in range(n)] for j in range(n)]
    for i in range(n):
        l[i][i]='X'
    for i in range(n):
        if s[i]=='1':
            for j in range(n):
                if l[i][j]==-1:
                    l[i][j]='='
                    l[j][i]='='
    for i in range(n):
        ok = 0
        for j in range(n):
            if ok==1:
                l[i][j]='-'
                l[j][i]='+'
            else:
                if l[i][j]==-1:
                    l[i][j]='+'
                    l[j][i]='-'
                    ok = 1 
    ok = 1
    for i in range(n):
        if s[i]=='1':
            if '-' in l[i]:
                ok = 0
                break 
        else:
            x = l[i].count('+')
            if x==0:
                ok = 0
                break 
    if ok==0:
        print("NO")
        return 
    print("YES")

    for i in l:
        print(''.join(i))
t = 1
t = ii()
for _ in range(t):
    solve()

