import sys,os,io
from sys import stdin
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left , bisect_right
import math 




alphabets = list('abcdefghijklmnopqrstuvwxyz')



#for deep recursion__________________________________________-
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc

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
    input = sys.stdin.readline
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline



def solve():
    n,m = li()
    s = si().strip()
    adj = [[] for i in range(n)]
    ind = [0]*n
    for i in range(m):
        x,y = li()
        x-=1
        y-=1
        adj[x].append(y)
        ind[y]+=1
    
    ancesstor = set()
    vis =  [False]*n 
    dp = [[0 for i in range(26)] for j in range(n)]
    @bootstrap
    def dfs(node):
        # print(node)
        ancesstor.add(node)
        for kid in adj[node]:
            if kid in ancesstor:
                print(-1)
                exit(0)
                yield -1
                
            if vis[kid]==False:
                vis[kid] = True
                yield dfs(kid)
            for j in range(26):
                dp[node][j] = max(dp[kid][j],dp[node][j])
        dp[node][ord(s[node])-97]+=1
        # if dp[node][ord(s[node])-97]==4:
        #     print("f")
        # print(dp[node][ord(s[node])-97])
        ancesstor.remove(node)  
        yield
    for i in range(n):
        if vis[i]==False:
            vis[i] = True 
            a = dfs(i)
            if a==-1:
                exit(0)
    ans = 0
    # print(dp)
    
    for i in dp:
        ans =max(ans,max(i))
    print(ans)

            

    


t = 1
# t = ii()
for _ in range(t):
    solve()
