n,m = [int(x) for x in input().split()]
l = []
a = 0
b = 1
k = min(n,m)
for i in range(min(n,m)+1):
    l.append([i,k-i])
    
print(len(l))
for i in l:
    print(*i)