import sys,os,io
import math 
from collections import defaultdict
from collections import deque
from typing import Union
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

def solve():
    n = ii()
    p = li()
    weights = li()
    parent = -1
    for i in range(n):
        p[i]-=1
        weights[i]-=1
        if p[i]==i:
            parent = i 
    disofnode = defaultdict(lambda:0)
    res = [0]*n 
    if weights[0]!=parent :
        print(-1)
        return 
    m = 0
    for i in range(1,n):
        node = weights[i]
        if p[node]!=parent and disofnode[p[node]]==0:
            print(-1)
            return 
        weightofparent = disofnode[p[node]]
        toadd = m - weightofparent + 1 
        # print(node,m)
        disofnode[node] = weightofparent+toadd
        m = weightofparent+toadd 
        res[node] = toadd 
    print(*res)






t = 1
t = ii()
for _ in range(t):
    solve()
