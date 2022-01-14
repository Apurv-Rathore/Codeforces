t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    ans = ''
    x = ['a','b','c']
    j = 0
    for i in range(n):
        
        ans+=x[j]
        j+=1
        j=j%3
    print(ans)
    