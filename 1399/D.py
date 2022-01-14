from collections import deque
for _ in range (int(input())):
    n = int(input())
    a = list(input())
    ans = [0]*(n)
    ans[0]=1
    one = deque()
    zero = deque()
    curr=1
 
    for i in range (n):
        if a[i]=='0':
            if len(one)>0:
                zero.append(one.pop())
                ans[i]=zero[-1]
            else:
                zero.append(curr)
                ans[i]=zero[-1]
                curr+=1
        else:
            if len(zero)>0:
                one.append(zero.pop())
            else:
                one.append(curr)
                curr+=1
            ans[i]=one[-1]
 
    print(max(ans))
    print(*ans)