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
from bisect import bisect_left , bisect_right
import math 


alphabets = list('abcdefghijklmnopqrstuvwxyz')


def isPrime(x):
    for i in range(2,x):
        if i*i>x:
            break
        if (x%i==0):
            return False
    return True
def ncr(n, r, p):  
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,p - 2, p)) % p
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
    c = dict(Counter(l))
    return list(set(l))
    # return c

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

#____________________GetPrimeFactors in log(n)________________________________________
def sieveForSmallestPrimeFactor():
    MAXN = 100001
    spf = [0 for i in range(MAXN)]
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
    for i in range(3, math.ceil(math.sqrt(MAXN))):
        if (spf[i] == i):
            for j in range(i * i, MAXN, i): 
                if (spf[j] == j):
                    spf[j] = i
    return spf
def getPrimeFactorizationLOGN(x):
    spf = sieveForSmallestPrimeFactor()
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]  
    return ret
#____________________________________________________________



def SieveOfEratosthenes(n): 
    #time complexity = nlog(log(n))
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime
def si():
    return input()
def divideCeil(n,x):
    #return (n+1)//x
    if (n%x==0):
        return n//x
    return n//x+1
def ii():
    return int(input())
def li():
    return list(map(int,input().split()))

#__________________________TEMPLATE__________________OVER_______________________________________________________


import sys,os,io
from math import gcd
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
import os
import sys
from io import BytesIO, IOBase
 
BUFSIZE = 8192
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    k = int(input())
    n = 2**k-1
    s = list(input().strip())
    s = s[::-1]
    q = ii()
    ans = [0]*(2**k)
    # for i in range(len(s)):
    #     if s[i]!='?':
    #         s[i]=str(abs(int(s[i])-1))
    for i in range(2**k-2,-1,-1):
        ans[i]=1
        if s[i]=='1':
            if i*2+1<n:
                ans[i]=ans[i*2+1]    
        if s[i]=='0':
            if i*2+2<n:
                ans[i]=ans[i*2+2]    
        if s[i]=='?':
            ans[i]=2
            if i*2+1<n:
                ans[i]=ans[i*2+1]    
            if i*2+2<n:
                ans[i]+=ans[i*2+2]
        
            
    # print(ans)
    for _ in range(q):
        ind,c = [x for x in input().split()]
        ind = int(ind)-1
        ind = 2**k-1 - ind - 1
        s[ind]=c 
        i = ind
        # print(s,i)
        if c=="0":
            if i*2+2<n:
                ans[i]=ans[i*2+2]    
            else:
                ans[i]=1 
        if c=="1":
            if i*2+1<n:
                ans[i]=ans[i*2+1]    
            else:
                ans[i]=1 
        if c=='?':
            ans[i]=2
            if i*2+1<n:
                ans[i]=ans[i*2+1]    
            if i*2+1<n:
                ans[i]+=ans[i*2+2]    
        ind=(ind-1)//2
        while(ind>=0):
            i = ind
            # print("ind",ind)
            ans[i]=1 
            c = s[i]
            if c=="0":
                if i*2+2<n:
                    ans[i]=ans[i*2+2]    
                else:
                    ans[i]=1 
            if c=="1":
                if i*2+1<n:
                    ans[i]=ans[i*2+1]    
                else:
                    ans[i]=1 
            if c=='?':
                ans[i]=2
                if i*2+1<n:
                    ans[i]=ans[i*2+1]    
                if i*2+1<n:
                    ans[i]+=ans[i*2+2]     
            ind=(ind-1)//2        
            # print(ind)
        # print(ans)
        print(ans[0])

t = 1
# t = ii()
for _ in range(t):
    solve()
