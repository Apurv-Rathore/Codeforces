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
    return l
    # return list(set(l))
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
def wia(a): sys.stdout.write(''.join([str(x) for x in a]) + '\n')

def nextPowerOf2(n):
 
    k = 1
    while k < n:
        k = k << 1
 
    return k
#__________________________TEMPLATE__________________OVER_______________________________________________________


if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = 1

# t = int(input())
for _ in range(t):
    n = ii()
    if (n==1):
        print(1,0)
        continue
    d = defaultdict(lambda:0)
    l = primeFactors(n)
    for i in l:
        d[i]+=1
    l = list(d.keys())
    res = 0
    pw2 = 10000000000000
    
    for i in l:
        x = d[i]
        c = 0
        while(x%2==0):
            x//=2
            c+=1
        pw2 = min(pw2,c)
        
    res = pw2
    for i in l:
        d[i]//=(2**pw2)
    minans = 1
    # print(l)
    # print(d)
    
    mx = 0
    temp = 0
    for i in l:
        # print(mx)

        mx = max(mx,nextPowerOf2(d[i]))
        # if (d[i]==1 and mx>1):
        #     mx = max(mx,nextPowerOf2(d[i]+1))
        toAdd = mx - d[i]
        if (toAdd>0):
            temp = 1
        minans*=i 
    for i in l:
        if (d[i]==1 and mx>1):
            mx = max(mx,nextPowerOf2(d[i]+1))
        toAdd = mx - d[i]
        if (toAdd>0):
            temp = 1
    #print(mx)
    # print(temp)
    if (mx>0):
        print(int(minans),int(res+log(mx,2)+temp))
    else:
        print(int(minans),int(res+temp))