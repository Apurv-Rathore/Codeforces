import sys,os,io
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = 1
# t = int(input())
for _ in range(t):
    n,l,r = [int(x) for x in input().split()]
    ansMin = 0
    x = 2
    for i in range(l-1):
        ansMin+=x
        x*=2 
    ansMin+=1
    ansMin+=n-l 


    ansMax = 0
    x = 2
    for i in range(r-1):
        ansMax+=x
        x*=2 
    x//=2
    ansMax+=1
    ansMax+=(n-r)*x 
    print(ansMin,ansMax)


