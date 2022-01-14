import os,sys
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
def funodd(n,a,b):
    if a>b:
        a,b=b,a
    minn = n//2-a 
    maxx = n//2+1+a 
    l = []
    for i in range(minn,maxx+1):
        l.append(i)
    return l 
def aa(a,b):
    return min(a,b),max(a,b)
for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    n = a+b 
    if n%2==0:
        a,b = aa(a,b)
        ans = []
        for i in range(n//2-a,n//2+a+1,2):
            ans.append(i)
        print(len(ans))
        print(*ans)
    else:
        ans = funodd(n,a,b)
        print(len(ans))
        print(*ans)
