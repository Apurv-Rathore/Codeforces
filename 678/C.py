import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
# t = int(input())
from sys import stdin
t = 1
for _ in range(t):
    n,a,b,p,q = [int(x) for x in input().split()]
    # n,k = list(map(int,stdin.readline().split()))
    x = lcm(a,b)
    if (p<q):
        c = ((n//a) - n//x )*p + (n//b)*q
        print(   c)
    else:
        c = ((n//b) - n//x )*q + (n//a)*p
        print(   c)
        