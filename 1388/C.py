import sys
sys.setrecursionlimit(10**6)
 
for _ in range(int(input())):
	n,m = map(int,input().split());p = list(map(int,input().split()));h = list(map(int,input().split()));	g=[[] for i in range(n)];an="YES";c=[0]*n
	for i in range(n-1):u,v = map(int,input().split());g[u-1].append(v-1);g[v-1].append(u-1)	
	def dfs(v,pa):	
		d=0
		for i in g[v]:
			if i!=pa:d+=dfs(i,v)
		c[v]=d+p[v]
		return c[v]
	dfs(0,-1)
	def df(v,pa):
		d=h[v];cr=c[v];bd=(cr-h[v])//2;gd=cr-bd;pos=1;aa=0;bb=0
		for i in g[v]:
			if i!=pa:kk=c[i];bh=(c[i]-h[i])//2;gh=c[i]-bh;aa+=gh;bb+=bh;pos=min(pos,df(i,v))
		if c[v]<abs(h[v]) or (cr-h[v])%2:return 0
		if aa<=gd and bb<=bd+(gd-aa):return pos
		return 0
	po=df(0,-1)
	if not po:an="NO"
	print(an)
