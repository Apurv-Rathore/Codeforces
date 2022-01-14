t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    if len(set(l))==1:
        print(n)
        continue
    if n==2 and l[0]==l[1]:
        print(2)
    else:
        print(1)