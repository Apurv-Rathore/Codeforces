t=int(input())
Maxn=210000
while(t>0):
	t-=1
	n,m=map(int,input().split())
	to=[[]]
	for i in range(0,n):
		to.append([])
	d=[0]*(n+1)
	ran=[0]*(n+1)
	q=[]
	cnt=0
	to[0].append(1)
	for i in range(0,m):
		bj,u,v=map(int,input().split())
		if(bj):
			(to[u]).append(v)
			d[v]+=1
			q.append((u,v))
		else:
			q.append((u,v))
	que=[]
	for i in range(1,n+1):
		if(d[i]==0): que.append(i)
	while(len(que)):
		now=que.pop()
		cnt+=1
		ran[now]=cnt
		for i in to[now]:
			d[i]-=1
			if(d[i]==0):
				que.append(i)
	if(cnt!=n):
		print("NO")
		continue
	print("YES")
	for i in q:
		if(ran[i[0]]<ran[i[1]]):
			print(i[0],i[1])
		else :
			print(i[1],i[0])