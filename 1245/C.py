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
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w")
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
def prefix_sum(arr):
    r = [0] * (len(arr)+1)
    for i, el in enumerate(arr):
        r[i+1] = r[i] + el
    return r
def divideCeil(n,x):
    if (n%x==0):
        return n//x
    return n//x+1
def si():
    return input()
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


#__________________________TEMPLATE__________________OVER_______________________________________________________

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = 1
# t = int(input())
for _ in range(t):
    s = list(input())
    n = len(s)
    if ('m' in s) or ('w' in s):
        print(0)
        continue
    if (len(s)==1):
        print(1)
        continue
    dp = [0]*(100001)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    mod = 1000000007
    if (n>=3):
        for i in range(3,n+1):
            dp[i]+=(dp[i-1]+dp[i-2])%mod
    res = 1
    
    curm = 0
    curw = 0
    for i in range(1,n):
        if (s[i]==s[i-1]=='n'):
            curw+=1
        elif (s[i]==s[i-1]=='u'):
            curm+=1
        else:
            res = (res*dp[curm+1])%mod
            res = (res*dp[curw+1])%mod
            curw = 0
            curm = 0
    if (s[-1]==s[-2]):
        res = (res*dp[curw+1])%mod
        res = (res*dp[curm+1])%mod
    print(res)