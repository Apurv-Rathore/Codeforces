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
def power_set(L):

    cardinality=len(L)
    n=2 ** cardinality
    powerset = []
    
    for i in range(n):
        a=bin(i)[2:]
        subset=[]
        for j in range(len(a)):
            if a[-j-1]=='1':
                subset.append(L[j])
        powerset.append(subset)
    powerset_orderred=[]
    for k in range(cardinality+1):
        for w in powerset:
            if len(w)==k:
                powerset_orderred.append(w)
        
    return powerset_orderred
def fastPlrintNextLines(a):
    # 12
    # 3
    # 1
    #like this
    #a is list of strings
    print('\n'.join(map(str,a)))

def sortByFirstAndSecond(A):
    A = sorted(A,key = lambda x:x[0])
    A = sorted(A,key = lambda x:x[1])
    return list(A)

#__________________________TEMPLATE__________________OVER_______________________________________________________


if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    n,k1,k2 = li()
    w,b = li()
    # print("_________________")
    whitepic = min(k1,k2)+abs(k1-k2)//2
    # blackpic =(2*n-whitepic*2)//2
    blackpic = (n-max(k1,k2))+abs(k1-k2)//2
    # print(k1,k2)
    # print(whitepic,blackpic)
    if w<=whitepic and b<=blackpic:
        print("YES")
    else:
        print("NO")



t = 1
t = int(input())
for _ in range(t):
    solve()
    