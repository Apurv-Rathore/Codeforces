t = int(input())
for _ in range(t):
	x,n=input().split()
	x=int(x)
	n=int(n)
	base=(n//4)*4
	for n in range(base+1,n+1):
		if(x%2==0):
			x=x-n
		else:
			x=x+n
	print(x)