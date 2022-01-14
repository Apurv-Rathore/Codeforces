#########################################################################################################\
#########################################################################################################
###################################The_Apurv_Rathore#####################################################
#########################################################################################################
#########################################################################################################
import sys,os,io
from sys import stdin
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math 
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
def ncr(n, r, p):  
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
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime
def countdig(n):
    c = 0
    while (n > 0):
        n //= 10
        c += 1
    return c
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
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def commonelement(a,b):
    c = 0
    for i in a:
        if (i in b):
            c+=1
    return c

t = 1
# t = int(input())
for _ in range(t):
    n = ii()
    a = li()
    l = []
    temp = []
    if (sum(a)==1):
        print(-1)
        continue
    divisors = [sum(a)]
    i = 2
    SumA = sum(a)
    while(i*i<=SumA):
        if (SumA%i==0):
            divisors.append(i)
            divisors.append(SumA//i)
        i+=1
    res = 100000000000000
    for k in divisors:
        if (SumA%k!=0):
            continue
        curSum = 0
        median = [-1]*n
        left = 0
        indexes = []
        for i in range(n):
            curSum+=a[i]
            if (a[i]==1):
                indexes.append(i)
            if (curSum==k):
                median[i] = indexes[(len(indexes)-1)//2]
                curSum = 0
                left = i+1
                indexes = []
        for i in range(n-2,-1,-1):
            if (median[i]==-1):
                median[i]=median[i+1]
        temp = 0
        # print(median)
        for i in range(n):
            if (a[i]==1):
                temp+=abs(median[i]-i)
        res = min(res,temp)
    print(res)

            
