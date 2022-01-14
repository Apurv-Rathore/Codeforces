from collections import defaultdict
t = int(input())
for _ in range(t):
    x = int(input())
    if (x>45):
        print(-1)
        continue
    k = 9
    s = []
    while(x>0):
        s.append(min(k,x))
        x-=min(k,x)
        k-=1
    dic = defaultdict(lambda:0)
    flag = 1
    for i in range(0,len(s)):
        dic[s[i]]+=1
        if (dic[s[i]]>1):
            flag = 0
            break 
    if (flag==0):
        print(-1)
        continue
    ans = ''
    for i in range(len(s)-1,-1,-1):
        ans+=str(s[i])
    print(int(ans))