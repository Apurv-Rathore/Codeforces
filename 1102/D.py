import math,sys
from sys import stdin, stdout
from collections import Counter, defaultdict, deque
input = stdin.readline
I = lambda:int(input())
li = lambda:list(map(int,input().split()))

def case():
    n=int(input())
    a=input().strip()
    a=list(a)
    zero,one,two=0,0,0
    for i in range(n):
        if(a[i]=='0'):
            zero+=1
        elif(a[i]=='1'):
            one+=1
        else:
            two+=1
    for i in range(n):
        if(a[i]=='1' and one>n//3 and zero<n//3):
            a[i]='0'
            one-=1
            zero+=1
        elif(a[i]=='2'):
            if(two>n//3 and zero<n//3):
                a[i]='0'
                two-=1
                zero+=1 
            elif(two>n//3 and one<n//3):
                a[i]='1'
                one+=1
                two-=1
    
    for i in range(1,n+1):
        if(a[-i]=='0'):
            if(zero>n//3 and two<n//3):
                a[-i]='2'
                two+=1
                zero-=1
            elif(zero>n//3 and one<n//3):
                a[-i]='1'
                zero-=1
                one+=1
        elif(a[-i]=='1'):
            if(one>n//3 and two<n//3):
                a[-i]='2'
                one-=1
                two+=1
        #print(a)
    print("".join(map(str,a)))

for _ in range(1):
    case()