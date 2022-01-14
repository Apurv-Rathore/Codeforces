import sys
sys.setrecursionlimit(100000)
l = list(input())
m = int(input())
ans = []
def fun(step, balance, weight):
    if (step==m):
        return 1
    #print("step,m",step,m,balance)
    if (balance>0):
        for i in range(len(l)):
            if (i+1==weight):
                continue
            if (l[i]=='1' and balance-i-1<0):
                ans.append(i+1)
                if (fun(step+1,balance-i-1,i+1)):
                    return 1
                ans.pop()
        return 0
    if (balance<0):
        for i in range(len(l)):
            if (i+1==weight):
                continue
            if (l[i]=='1' and balance+i+1>0):
                ans.append(i+1)
                if (fun(step+1,balance+i+1,i+1)):
                    return 1
                ans.pop()
        return 0
    if (balance==0):
        for i in range(len(l)):
            
            if (l[i]=='1'):
                
                ans.append(i+1)
                if (fun(step+1,balance+i+1,i+1)):
                    return 1
                ans.pop()
        return 0
if (fun(0,0,0)):
    print("YES")
    print(*ans)
else:
    print("NO")