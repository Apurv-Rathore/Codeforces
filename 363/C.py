l = list(input())
c = 1
res = 0
n = len(l)
ans = [l[0]]
for i in range(1,n):
    if (l[i]==l[i-1]):
        if (c==1):
            if len(ans)>2 and ans[-2]==ans[-3]:
                continue
        if (c==2):
            continue
        c+=1
        ans.append(l[i])
    else:
        c = 1
        ans.append(l[i])
s = ''
for i in ans:
    s+=i
print(s)
        
        