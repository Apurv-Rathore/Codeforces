import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
n = int(input())
a = [int(i) for i in input().split()]
m = 0
mi = 0
b = [-1]*(35)
for i in range (len(a)):
    bi = bin(a[i])[2:][::-1]
    for j in range (len(bi)):
        if bi[j]=='1':
            if b[j]==-1:
                b[j] = i
            elif b[j]>=0:
                b[j] = -2
for i in range(34,-1,-1):
    if b[i]>=0:
        a[b[i]],a[0] = a[0],a[b[i]]
        break
print(*a)