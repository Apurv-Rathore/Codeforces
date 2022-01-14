import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n = int(input())
    cur = [int(i) for i in input().split()]
    ans = cur[2]
    curL = cur[0]
    curR = cur[1]
    ansL = ans
    ansR = ans
    singleL = cur[0]
    singleR = cur[1]
    print(ans)
    for i in range (n-1):
        c = [int(i) for i in input().split()]
        if c[0]==singleL and c[1]==singleR:
            ans = min(ans, c[2])
        elif c[0]<=singleL and c[1]>=singleR:
            ans = c[2]
            singleR = c[1]
            singleL = c[0]
        if c[0]<curL:
            curL = c[0]
            ansL = c[2]
        if c[1]>curR:
            curR = c[1]
            ansR = c[2]
        if c[0]==curL and c[2]<ansL:
            curL = c[0]
            ansL = c[2]
        if c[1]==curR and c[2]<ansR:
            curR = c[1]
            ansR = c[2]
        if singleL == curL and singleR == curR:
            print(min(ans, ansL + ansR))
        else:
            print(ansL + ansR)