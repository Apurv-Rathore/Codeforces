import os,sys
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
from math import log2 as l2
t = int(input())
for _ in range(t):
    d,m = [int(x) for x in input().split()]
    bit = l2(d)
    bit = int(bit)+1
    ans = 1
    # print("bit",bit)
    p = 0
    for i in range(0,bit+1):
        if (1<<(i))>d:
            break
        ans = ans * (min(2**(i+1) -1 , d) - 2**(i) + 2)
    ans-=1
    print(ans%m)
