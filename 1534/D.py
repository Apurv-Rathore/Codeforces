e = set()
def ae(i,j):
    e.add((min(i,j),max(i,j)))
 
def q(c):
    print('?',c+1,flush=1)
    d = [int(i) for i in input().split()]
    for i in range (n):
        if d[i]==1:
            ae(c+1,i+1)
    return d
            
n = int(input())
d = q(0)
ev = []
od = []
for i in range (n):
    if d[i]%2:
        od.append(i)
    elif d[i]!=0:
        ev.append(i)
f=od
if len(ev)<len(od):
    f=ev
for i in f:
    q(i)
print('!')
for i in e:
    print(*i,flush=1)