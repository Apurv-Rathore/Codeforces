import bisect
n,s = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
l.sort()
x = s
ans = 0
while(l[(n+1)//2 -1]!=x):
    # print(bisect.bisect(l,x))
    l.insert(bisect.bisect_left(l,x),x)
    ans+=1
    n+=1
    # print(l,n,l[(n+1)//2 -1])
print(ans)
