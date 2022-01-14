from heapq import heappush as hp, heappop as hpop
for t in range(int(input())):
	n = int(input())
	a = [0]*n
	h = []
	hp(h,(-n,(0,n-1)))
	i = 1
	for i in range(1,n+1):
		s,(l,r) = hpop(h)
		j = (r+l)//2
		a[j] = i
		hp(h,(-(j-l),(l,j-1)))
		hp(h,(-(r-j),(j+1,r)))
	print(*a)	
