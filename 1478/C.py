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


def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')


t = 1
t = int(input())
for _ in range(t):
    n = ii()
    d = li()
    l = []
    dic = defaultdict(lambda:0)
    for i in d:
        dic[i]+=1
    f = 0
    for i in dic.keys():
        if dic[i]==2:
            l+=[i]*(dic[i]//2)
        else:
            f = 1
            break
    if (f==1):
        print("NO")
        continue
    l.sort()
    an = 0
    ite = 0
    ans = []
    # print(l)
    for i in range(n-1,-1,-1):
        #2nan = l[i]
        if (l[i])%(2)!=0:
            f = 1
            break
        else:
            if (((l[i]//2) - an)%(n-ite))!=0:
                f = 1
                break
            else:
                if (((l[i]//2) - an)//(n-ite)<=0):
                    f = 1
                    break    
                an += ((l[i]//2) - an)//(n-ite)
                ite+=1
    # print(ans)
    if (f==0):
        print("YES")
        
    else:
        print("NO")


