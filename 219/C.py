from sys import stdin
input = stdin.readline
def put(): return map(int, input().split())

n,k = put()
s = [ord(i)-ord('A') for i in list(input())]

ans = []
dp = [0]*k
ans.append(dp)
a = b = 0
for i in range(n):
    tmp = []
    first, second = n+1, n+1
    for j in range(k):
        if dp[j]==a:
            y = b
        else:
            y = a
        x = y + (0 if s[i]==j else 1)
        if first>x:
            second = first
            first = x
        elif second>x:
            second = x
            pass
        tmp.append(x)
    a,b = first,second
    dp = tmp
    ans.append(tmp)

l = []
x = min(dp)

prev = -1
for i in range(n,0,-1):
    if prev !=-1:
        ans[i][prev]=n+1
    #print(ans[i])
    a = ans[i].index(x)
    l.append(chr(a+ord('A')))
    if s[i-1] != a:
        x-=1
    prev = a
    


print(min(dp))
y = ''.join(l[::-1])
print(y)

        
    

