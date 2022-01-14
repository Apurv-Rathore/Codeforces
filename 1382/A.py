from collections import defaultdict
t = int(input())
for _ in range(t):
#    n = int(input())
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dic_a = defaultdict(lambda :0)
    for i in a:
        dic_a[i]+=1
    tmp=0
    for i in b:
        if dic_a[i]!=0:
            print("YES")
            print(1,i)
            tmp=1
            break
    if tmp==0:
        print("NO")
   
