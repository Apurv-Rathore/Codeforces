#########################################################################################################\
#########################################################################################################
###################################The_Apurv_Rathore#####################################################
#########################################################################################################
#########################################################################################################

import sys,os,io
from math import log, gcd, ceil
from collections import defaultdict as dd, deque, Counter
from heapq import heappush, heappop
from sys import stdin
from bisect import bisect_left, bisect_right 
import math 



def ncr(n, r, p):  #using fermat's little theorem
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,
                      p - 2, p)) % p

  
def primeFactors(n): 
    l = []
    while n % 2 == 0: 
        l.append(2)
        n = n / 2
          
    for i in range(3,int(math.sqrt(n))+1,2): 
          

        while n % i== 0: 
            l.append(int(i))
            n = n / i 
    if n > 2: 
        l.append(n)
    return list(set(l))
    
def power(x, y, p) : 
	res = 1
	x = x % p 
	if (x == 0) : 
		return 0
	while (y > 0) : 
		if ((y & 1) == 1) : 
			res = (res * x) % p 
		y = y >> 1	 # y = y/2 
		x = (x * x) % p 		
	return res 


def si():
    return input()

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def prefix_sum(arr):
    r = [0] * (len(arr)+1)
    for i, el in enumerate(arr):
        r[i+1] = r[i] + el
    return r

def divideCeil(n,x):
    if (n%x==0):
        return n//x
    return n//x+1

def ii():
    return int(input())

def li():
    return list(map(int,input().split()))

def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")


# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

mod = 998244353 


tt = 1
tt= ii()
for _ in range(tt):
    s = si()
    t = si()
    d = dd(lambda:-1)
    n = len(s)
    
    l = [[-1 for i in range(26)] for j in range(n)]
    for i in range(n):
        l[i][ord(s[i])-97] = i
        if (i<n-1):
            for j in range(26):
                    l[i+1][j] = l[i][j]
    ptr = len(s)-1
    i = len(t)-1
    c = 0
    f = 0
    while(i>=0):
        # print("i,ptr",i,ptr)
        if (ptr==-1):
            ptr = l[-1][ord(t[i])-97]
            c+=1
        else:

            ptr = l[ptr][ord(t[i])-97]
        # print("i,ptr",i,ptr)
        if (ptr==-1):
            ptr = l[-1][ord(t[i])-97]

            if (ptr==-1):
                f = 1
                break
            c+=1
        if (t[i]==t[i-1]):
            ptr-=1
        i-=1
    if (f==1):
        c = -2
    print(c+1)
        
    