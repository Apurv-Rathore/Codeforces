import sys,os,io
from math import log, gcd
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop

import math 

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

t = int(input())
for _ in range(t):
    n = ii()
    l = li()
    if (sum(l)!=0 and l.count(0)==0):
        print(0)
    elif (sum(l)!=0 and l.count(0)!=0):
        x = l.count(0)
        if sum(l)+x==0:
            print(x+1)
        else:
            print(x)
    elif (sum(l)==0 and l.count(0)==0):
        print(1)
    elif (sum(l)==0 and l.count(0)!=0):
        print(l.count(0))






