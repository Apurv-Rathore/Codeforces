from sys import stdin
t = int(stdin.readline())
#t = int(input())
for _ in range(t):
    n,m,x,y = map(int,stdin.readline().split())
#    n,m,x,y = [int(x) for x in input().split()]
    if y>2*x:
        y=2*x
    ans=0
    for i in range(n):
        l = input()
        flag=0
        for j in range(m):
            if l[j]=='.' and flag==0: #this shows that this . is not included in y
                if j!=m-1 and l[j+1]=='.':
                    ans+=y
                    flag=1
                else:
                    ans+=x
            elif flag==1:
                flag=0
    print(ans)
                