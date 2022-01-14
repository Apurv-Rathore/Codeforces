from collections import defaultdict, deque, Counter
from sys import stdin, stdout
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
        n = n / 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            l.append(int(i))
            n = n / i
    if n > 2:
        l.append(n)
    return list(set(l))


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
    return [int(x) for x in input().split()]

def sapin():
    return [int(x) for x in input()]

#?############################################################


input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = 1
m  = 1000000007
mm = ["YES", "NO"]
for _ in range(t):
    n = int(input())
    a = mapin()
    ans = 0
    d = [0]*(n+1)
    temp = 0
    for i in range(n):
        temp+=a[i]
        d[i+1] = temp

    # print(d)
    dd = set()
    dd.add(0)
    i = 0
    j = 0
    while(i<n):
        while(j<n):
            if(d[j+1] in dd):
                break
            else:
                # print(i, j, "dpe")
                dd.add(d[j+1])
                # ans+=1
                j+=1

        ans+=j
        ans-=i
        dd.remove(d[i])
        # print(i, dd)
        # print(i, j)
        i+=1
        # print(i, "dssas")

    print(ans)

   