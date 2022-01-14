#########################################################################################################\
#########################################################################################################
###################################The_Apurv_Rathore#####################################################
#########################################################################################################
#########################################################################################################
import sys,os,io
from sys import stdin
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
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


if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def fun(n):
    if math.sqrt(n)==int(math.sqrt(n)):
        return 1
    return 0


def find(v,parent):
    if v==parent[v]:
        return v 
    parent[v]=find(parent[v],parent)
    return parent[v]


def union(a,b,parent):
    a = find(a,parent)
    b = find(b,parent)
    if a!=b:
        if parent[b]<parent[a]:
            parent[a]=parent[b]
            return 1
        else:
            parent[b]=parent[a]
            return 0

def solve():
    n,l,r = li()
    socks = li()
    ls = socks[:l]
    rs = socks[l:]
    if l>r:
        l,r = r,l 
        s = ls[:]
        ls = rs[:]
        rs = s[:]
    toShift = (r-l)//2 
    d = defaultdict(lambda:0)
    
    for i in rs:
        d[i]+=1
    
    d1 = defaultdict(lambda:0)
    for i in ls:
        d1[i]+=1
    
    for i in list(list(d1.keys())+list(d.keys())):
        m = min(d[i],d1[i])
        d[i]-=m
        d1[i]-=m 
        l-=m 
        r-=m 
    toShift = (r-l)//2 
    
    # print(d)
    ans = toShift
    # print(toShift)
    cnt=0
    for i in d.keys():
        x = (d[i]//2)
        m = min(x,toShift)
        # print(i,m)
        d[i]-=m 
        toShift-=m 
        cnt+=m
        # ans+=m
        if toShift==0:
            # print(ans)
            break 
    ans = ans + (l+r)//2-cnt
    # ans+=toShift

    print(ans)







t = 1
t = int(input())
for _ in range(t):
    solve()
    
