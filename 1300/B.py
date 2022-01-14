import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
for _ in range (int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    print(a[n]-a[n-1])