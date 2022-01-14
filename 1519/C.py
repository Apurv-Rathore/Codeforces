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

def solve():
    n = ii()
    u = li()
    s = li()
    un = [[] for i in range(n+1)]
    d = defaultdict(list)
    for i in range(n):
        un[u[i]].append(s[i])
    u = un[:]
    xx = defaultdict(lambda:0)
    for i in range(1,n+1):
        if u[i]==[]:
            continue
        u[i].sort(reverse=True)
        suf = [0]*len(u[i])
        summ = 0
        for j in range(len(u[i])-1,-1,-1):
            summ+=u[i][j]
            if j==len(u[i])-1:
                suf[j]=u[i][j]
            else:
                suf[j]=u[i][j]+suf[j+1]
        suf = suf[::-1]
        d[i]=suf
        xx[i]=summ
    # print(d)
    # print(xx)
    # print(u)
    temp = [0]*(n+1)
    for i in range(n+1):
        if u[i]==[]:
            continue
        for j in range(1,n+1):
            if (j>len(u[i])):
                break
            mod = len(u[i])%j
            ans = 0
            if mod!=0:
                ans+=xx[i]-d[i][mod-1]
            else:
                ans+=xx[i]
            temp[j]+=ans
    temp = temp[1:]
    print(*temp)
    # for j in range(1,n+1):
    #     ans = 0
    #     # print("f")

    #     # print(j,"f",n)
    #     # print(u)
    #     for i in range(n+1):

    #         if u[i]==[]:
    #             continue
    #         # print(j,len(u[i]),i)
    #         if j>len(u[i]):
    #             break
    #         # print("h")
    #         mod = len(u[i])%j
    #         if j==3:
    #             print("f",u[i],mod,xx[i],d[i],mod)
    #         if mod!=0:
    #             # if j==3:
    #             #     print("f",xx)
    #             ans+=xx[i]-d[i][mod-1]
    #         else:
    #             ans+=xx[i]
    #         # print(ans,"f")
    #     print("duck",ans,end=" ")
    # print()
        


t = 1
t = int(input())
for _ in range(t):
    solve()
    
