n,p = [int(x) for x in input().split()]
l = list(input())
flag = 0
if (p>n//2):
    flag = 1
ans = 0
p-=1
ff = p
ffm = p
for i in range(n):
    if (i>n-i-1):
        break
    x = ord(l[i])-97
    y = ord(l[n-i-1])-97
    if (x!=y):
        ans += min(abs(x-y) , 26-max(x,y) + min(x,y))
        if (abs(p-i)<abs(p-(n-i-1))):
            temp = i
        else:
            temp = n-i-1
        ff = max(ff,temp)
        ffm = min(ffm,temp)
x = abs(p-ff)
y = abs(p-ffm)
res = min(x,y)*2+max(x,y)
print(ans + res)
    
