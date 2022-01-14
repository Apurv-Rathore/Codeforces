# \
#########################################################################################################
###################################The_Apurv_Rathore#####################################################
#########################################################################################################
#########################################################################################################
import sys
import os
import io
from sys import stdin
from math import log, gcd, ceil
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math
from bisect import bisect_left , bisect_right
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


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
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


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


def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


t = 1
t = int(input())
for _ in range(t):
    n = ii()
    a = []
    for i in range(n):
        a.append(list(input()))
    aa = input()
    b = []
    for i in range(n):
        b.append(list(input()))

    l = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            l[i][j] = int(a[i][j])^int(b[i][j])
    temp = l[0]
    temprev = []
    for i in range(n):
        temprev.append((abs(int(temp[i])-1)))
    f = 0

    for i in range(n):
        if (l[i]==temp):
            continue
        elif l[i]==temprev:
            l[i] = temp
        else:
            # print("i",i)
            f = 1
            break
    if (f==1):
        print("NO")
        continue
    # print("---------")
    # for h in l:
    #     print(h)
    # print(l)
    # print("---------")

    temp = []
    for i in range(n):
        temp.append(l[i][0])
        # print("l[0][i]",l[0][i],i)
    temprev = []
    for i in range(n):
        temprev.append((abs(int(temp[i])-1)))
    # print("temp",temp)
    # print("temprev",temprev)
    for j in range(n):
        x = []
        for i in range(n):
            x.append(l[i][j])
        # print("x",x)
        if (x==temp):
            continue
        elif x==temprev:
            for h in range(n):
                l[h][j]=temp[h]
        else:
            f = 1
            break
    if (f==0):
        print("YES")
    else:
        print("NO")
