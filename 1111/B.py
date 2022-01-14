n,k,m = list(map(int,input().split()))
l = list(map(int,input().split()))
res = 0;avg = sum(l)/n;s = sum(l)
l.sort()
for i in range(min(n,m+1)):
    if (i>0):
        s-=l[i-1]
    left = m - i
    temp = min(left,k*(n-i))
    
    res = max (res , (s+temp)/(n-i) )
    
print(res)
