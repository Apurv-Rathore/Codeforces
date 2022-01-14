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

n,k = li()
p = li()
group = [-1]*256
ans = []
for i in range(n):
    if group[p[i]]!=-1:
        ans.append(group[p[i]])
        continue
    prev = -1
    for j in range(p[i],-1,-1):
        if j == p[i] - k :
            break
        if group[j]!=-1:
            if k - (j - group[j]+1) - (p[i] - j) <0:
                break
            prev = j 
            break 
    y = -1
    for j in range(p[i],-1,-1):
        if group[j]!=-1:
            y = j 
            break 
    if prev==-1:
        val = max(y+1,p[i]-k+1)
        ind = - 1 
        for j in range(max(y+1,p[i]-k+1),p[i]+1):
            group[j] = val
        ans.append(val)
    else:
        for j in range(prev+1,p[i]+1):
            group[j] = group[prev]
        ans.append(group[p[i]])
# print(*group)

for i in range(256):
    if group[i]==-1 and i>0 and group[i-1]>=0:
        if (i-1) - group[i-1] + 1 <k:
            group[i] = group[i-1]
        
cnt = 0
prev = -1
for i in range(256):
    if group[i]==-1:
        if cnt==k or prev==-1:
            cnt = 1 
            group[i] = i 
            prev  = i 
        else:
            cnt += 1 
            group[i] = prev 
    else:
        cnt = k



# print(*group)
print(*ans)


# def solve (N, R, S, Marks):
#     # write your code here
#     pass
 
# N = int(input())
# R = int(input())
# S = int(input())
# Marks = list(map(int, input().split()))
 
# out_ = solve(N, R, S, Marks)
# for i_out_ in out_:
#     print (' '.join(map(str, i_out_)))