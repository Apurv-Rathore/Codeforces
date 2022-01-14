from sys import stdin
input=lambda : stdin.readline().strip()
from math import ceil,sqrt,factorial,gcd
for _ in range(int(input())):
	n,k=map(int,input().split())
	s=sorted(list(input()))
	if n==k:
		print(s[-1])
	elif s[0]!=s[k-1]:
		print(s[k-1])
	elif s[-1]==s[k]:
		print(s[0]+s[k]*((n-1)//k))
	else:
		print(*s[k-1:],sep="")