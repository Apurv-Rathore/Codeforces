import sys,os,io
from sys import stdin
from bisect import bisect_left
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n,h,l,r = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
for i in range(1,n):
	a[i]+=a[i-1]
dp = [[-1 for i in range(n+1)] for j in range(n+1)]

def rec(i,j):
	#i,j indicates the number of maximum times good sleep with j already late slept
	if i==n:
		return 0
	if dp[i][j]!=-1:
		return dp[i][j]
	sleepingTime = a[i]-j 
	sleepingTime%=h
	temp = 0
	if l<=sleepingTime<=r:
		temp = 1
	ans1 =  temp + rec(i+1,j)

	sleepingTime = a[i]-j-1
	sleepingTime%=h
	temp = 0
	if l<=sleepingTime<=r:
		temp = 1
	
	ans2 =  temp + rec(i+1,j+1)
	dp[i][j] = max(ans1,ans2)
	return dp[i][j]
# print(dp)
print(rec(0,0))

	


