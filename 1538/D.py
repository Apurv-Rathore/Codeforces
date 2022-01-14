from collections import defaultdict, deque, Counter
import sys
from heapq import heappush, heappop
import math
import io
import os
import math
import bisect

#?############################################################


def isPrime(x):
    for i in range(2, x):
        if i*i > x:
            break
        if (x % i == 0):
            return False
    return True

#?############################################################


def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


#?############################################################

def primeFactors(n):
    l = []
    while n % 2 == 0:
        l.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            l.append(i)
            n = n // i
    if n > 2:
        l.append(n)
    return l


#?############################################################

def power(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

#?############################################################


def sieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime


#?############################################################

def digits(n):
    c = 0
    while (n > 0):
        n //= 10
        c += 1
    return c

#?############################################################


def ceil(n, x):
    if (n % x == 0):
        return n//x
    return n//x+1

#?############################################################


def mapin():
    return map(int, input().split())

#?############################################################


if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

N = int(math.sqrt(1000000000))+10
spf = [0]*N
primes = []
for i in range(2,N):
    if spf[i]==0:
        primes.append(i)
        for j in range(i,N,i):
            spf[j]=i
# for i in range(2,N):
#     if spf[i]==0:
#         primes.append(i)
# print(primes[-1])
def noOfFact(n):
    cnt = 0
    for i in primes:
        while n%i==0:
            cnt+=1
            n//=i 
    if n>1:
        cnt+=1
    return cnt


t  = int(input())
for _  in range(t):
    a,b,k = [int(x) for x in input().split()]
    mn = 2
    
    if a!=b and (a%b==0 or b%a==0):
        mn = 1
    na = noOfFact(a)
    nb = noOfFact(b)
    # print(na,nb,k)
    if mn<=k<=na+nb:
        print("YES")
    else:
        print("NO")
