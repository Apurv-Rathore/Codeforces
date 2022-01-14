import bisect
n=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
x=[0]*n
for i in range(len(a)):
	x[i]=a[i]-b[i]
x.sort()
ans=0
for i in range(n):
	if x[i]<=0:
		continue
	else:
		ans+=i-bisect.bisect_left(x,-x[i]+1)
print(ans)









