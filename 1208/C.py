#########################################################################################################\
#########################################################################################################
###################################The_Apurv_Rathore#####################################################
#########################################################################################################
#########################################################################################################
import sys,os,io
from sys import stdin
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop,heapify
from bisect import bisect_left , bisect_right
import math 

# sys.setrecursionlimit(100000)
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
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    n = ii()
    l = [[0 for i in range(4)] for j in range(4)]
    c = 0
    f = 0
    for i in range(4):
        if f==0:
            f = 1
            for j in range(4):
                l[i][j]=c
                c+=1
        else:
            f = 0
            for j in range(4-1,-1,-1):
                l[i][j]=c
                c+=1
    ans = [[0 for i in range(n)] for j in range(n)]
    i = 0
    j = 0
    prev = 0
    while(i<n):
        # print(i,j,n)
        

        # for ie in ans:
        #     print(*ie)
        p1 = 0
        for iii in range(i,i+4):
            for jjj in range(j,j+4):
                # print(iii,jjj)
                ans[iii][jjj]=l[iii-i][jjj-j]+prev 
                p1 = max(ans[iii][jjj],p1)
        prev = p1+1
        j+=4
        if j==n:
            j = 0
            i+=4
        



    for i in ans:
        print(*i)

    




    
        



t = 1
# t = int(input())
for _ in range(t):
    solve()
    
