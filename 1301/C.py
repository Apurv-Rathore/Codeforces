import sys
import os
import io
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop


import math


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


def power(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0):
        if ((y & 1) == 1):
            res = (res * x) % p
        y = y >> 1	 # y = y/2
        x = (x * x) % p
    return res


def si():
    return input()

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def prefix_sum(arr):
    r = [0] * (len(arr)+1)
    for i, el in enumerate(arr):
        r[i+1] = r[i] + el
    return r


def divideCeil(n, x):
    if (n % x == 0):
        return n//x
    return n//x+1


def ii():
    return int(input())


def li():
    return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    n, m = li()
    noOfZerosCons = (n-m)//(m+1)
    howManyOneMore = (n-m) % (m+1)
    ans = 0
    ans = ans + (noOfZerosCons*(noOfZerosCons+1)//2)*(m+1-howManyOneMore)
    ans = ans + howManyOneMore*((noOfZerosCons+1)*(noOfZerosCons+2)//2)
    print(n*(n+1)//2 - ans)
