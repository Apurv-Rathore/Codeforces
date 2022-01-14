from math import *
from collections import defaultdict
# Function to find the nCr
 
 
def ncr(n, r):
 
    # p holds the value of n*(n-1)*(n-2)...,
    # k holds the value of r*(r-1)...
    p = 1
    k = 1
 
    # C(n, r) == C(n, n-r),
    # choosing the smaller value
    if (n - r < r):
        r = n - r
 
    if (r != 0):
        while (r):
            p *= n
            k *= r
 
            # gcd of p, k
            m = gcd(p, k)
 
            # dividing by gcd, to simplify product
            # division by their gcd saves from 
            # the overflow
            p //= m
            k //= m
 
            n -= 1
            r -= 1
 
        # k should be simplified to 1
        # as C(n, r) is a natural number
        # (denominator should be 1 )
 
    else:
        p = 1
 
    # if our approach is correct p = ans and k =1
    return p
 
from sys import stdin
from math import log,ceil
# t = int(input())
dic = defaultdict(str)
t = 1

def fun(l,length):
    # print(set(l[1:]))
    # print(l)
    if (set(l[1:])==set([0])):
        return 0
    if (length==1):
        return 1
    s = ''
    for i in l:
        s+=str(i)
    if (dic[s]==1):
        return 0
    dic[s]=1
    ans1 = factorial(length)
    temp = factorial(length-1)
    
    for i in range(10):
        if (l[i]>0):
            ans1/=factorial(l[i])
            
            if (i==0):
                
                temp/=factorial(max(1,l[i]-1))
            else:
                temp/=factorial(l[i])
    # print(ans1,temp)
    if (l[0]>0):
        ans1 = ans1 - temp
    for i in range(10):
        if (l[i]>1):
            l1 = l[:]
            l1[i]-=1
            ans1+=fun(l1,length-1)
    return ans1
ans = 0
for _ in range(t):
    n = list(input())
    l = [0]*10
    for i in n:
        l[int(i)]+=1 
    print(int(fun(l,len((n)))))
    