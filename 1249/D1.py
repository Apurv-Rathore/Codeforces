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


if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

fk = [-1]*50
def fun(n,dp,u):
    print(fk)
    if n>=0:
        if fk[n]!=-1:
            return fk[n]
    dp = dp[:]
    if n>=0 and check(dp,u,n)==True:
        fk[n]=True
        return True
    if n<=0:
        return False
    # print(n,dp)
    dp[n]-=1
    dp[n-1]+=1
    if n>=2:
        dp[n-2]+=1
    fk[n]=fun(n-2,dp,u) or fun(n-1,dp,u)
    return fk[n]

def check(dp,u,n):
    dp=dp[1:]
    for i in range(n+1):
        if dp[i]<u[i]:
            return False
    return True 

def fun(covered,k,right):
    f = 0
    maxCnt = 0
    maxEl = -1
    cntArr = [0]*201
    for i in range(len(covered)):
        if len(covered[i])<=k:
            continue
        else:
            for j in covered[i]:
                cntArr[j]=right[j]
            f = 1
            break
    if f==0:
        return -1
    maxEl=cntArr.index(max(cntArr))
    return maxEl
def solve(_):
    n,k = li()
    covered = [[] for i in range(201)]
    right = [0]*201
    for i in range(n):
        l,r = li()
        l-=1
        r-=1
        right[i]=r
        for j in range(l,r+1):
            covered[j].append(i)
    back = covered[:]
    rem = []
    while(1):
        x = fun(covered,k,right)
        if x==-1:
            break 
        rem.append(x+1)
        for j in range(len(covered)):
            if x in covered[j]:
                covered[j].remove(x)
    # print(covered)
    print(len(rem))
    print(*rem)

        



t = 1
# t = int(input())
for _ in range(t):
    solve(_)
    
