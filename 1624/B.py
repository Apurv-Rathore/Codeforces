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

def fun(a,b):
    if a and b and abs(a)//a==abs(b)//b:
        return 1
    return 0

def solve():
    a,b,c = li()


    # mc = 2b-a


    if (2*b-a)%c==0 and fun(2*b-a,c):
        print("YES")
        # print("f")
        return



    if (2*b-c)%a==0 and fun(2*b-c,a):
        print("YES") 
        return

    mb = (a+c)//2 

    if (a+c)%2==0 and ((a+c)//2)%b==0 and fun(a+c,b):
        print("YES")
        return
    print("NO")

    
             



        



t = 1
t = ii()
for _ in range(t):
    solve()
