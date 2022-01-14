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
import math 
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
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
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def commonelement(a,b):
    c = 0
    for i in a:
        if (i in b):
            c+=1
    return c

t = 1
# t = int(input())
for _ in range(t):
    n = ii()
    l = []
    d = defaultdict(list)
    for i in range(n-2):
        x = li()
        d[x[0]].append(i)
        d[x[1]].append(i)
        d[x[2]].append(i)
        l.append(x)
    firstelement = 0
    for i in d.keys():
        if (len(d[i])==1):
            firstelement = i
    temp = l[d[firstelement][0]][:]
    temp.remove(firstelement)
    other1 = temp[0]
    other2 = temp[1]
    if (len(d[other1])>len(d[other2])):
        other1,other2 = other2, other1
    ans = [firstelement,other1,other2]
    prev = d[firstelement][0]
    # #print(l)
    # #print(d[1])
    while(len(ans)<n):
        #print(ans)
        x = d[other2]
        #print(x,prev)
        x.remove(prev)
        # #print(x)
        if (len(x)==1):
            xx = l[x[0]][:]
            xx.remove(ans[-1])
            xx.remove(ans[-2])
            ans.append(xx[0])
            continue
            # break
        temp1 = l[x[0]][:]
        temp2 = l[x[1]][:]
        c1 = commonelement(temp1,l[prev])
        c2 = commonelement(temp2,l[prev])
        # #print("c1,c2",c1,c2)
        if (c1>c2):
            temp1.remove(ans[-1]) 
            temp1.remove(ans[-2]) 
            ans.append(temp1[0])
            other2 = temp1[0]
            prev = x[0]
        else:
            temp2.remove(ans[-1]) 
            temp2.remove(ans[-2]) 
            ans.append(temp2[0])
            other2 = temp2[0]
            prev = x[1]
        # #print("newprv",prev)
    print(*ans)

    