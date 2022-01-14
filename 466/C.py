# x,y = [int(x) for x in stdin.readline().split()]
n = int(input())
a = [int(x) for x in input().split()]
cnt = [0]*n
sums = [0]*n
temp = 0
s = sum(a)
ans = 0
if (s%3==0):
    for i in range(n-1,-1,-1):
        temp+=a[i]
        if (temp==s/3):
            cnt[i]=1
    for i in range(n-2,-1,-1):
        cnt[i]+=cnt[i+1]
    temp = 0
    for i in range(n-2):
        temp+=a[i]
        if (temp==s/3):
            ans+=cnt[i+2]
print(ans)