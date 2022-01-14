t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    s = input()
    l = list(s)
#    l = l+l
    for i in range(k):
        l.append(l[n +i-k])
    n = len(l)
    flag = 0
    for i in range(n-k):
        if (l[i]=='?' and l[i+k]!='?') or (l[i]!='?' and l[i+k]=='?'):
            if (l[i]=='?' and l[i+k]!='?'):
                l[i] = l[i+k]
            else:
                l[i+k] =l[i]
        else:
            if l[i]=='?' and l[i+k]=='?':
                continue
            else:
                if l[i]!=l[i+k]:
                    flag = 1
                    break
    count0 = l[:k].count('0')
    count1 = l[:k].count('1')
    countq = l[:k].count('?')
    i = k-1
    
    if count1>k//2 or count0>k//2:
        flag = 1
    for i in range(k,n-k):
#        print(count0,count1,countq)
        if l[i-k]=='0':
            count0-=1
        elif l[i-k]=='1':
            count1-=1
        else:
            countq-=1
        if l[i]=='0':
            count0+=1
        elif l[i]=='1':
            count1+=1
        else:
            countq+=1
        if count1>k//2 or count0>k//2:
            flag = 1
    if flag==1:
        print("NO")
    else:
        print("YES")
        