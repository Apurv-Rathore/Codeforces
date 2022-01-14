import sys,os,io
import bisect
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for _ in range (int(input())):
    n = int(input())
    a = []
    h1 = []
    w1 = []
    a1 = []
    for i in range (n):
        h,w = [int(i) for i in input().split()]
        a.append([h,w,i])
        a1.append([w,h,i])
        h1.append(h)
        w1.append(w)
    a.sort()
    h = []
    sw = []
    hw = []
    mw = 10**10
    mw1 = 10**10
    for i in a:
        h.append(i[0])
        if mw> i[1]:
            mw = i[1]
            sw.append([mw, i[2]])
        else:
            sw.append([mw,sw[-1][1]])

    ans = []
    for i in range (n):
        ind = bisect.bisect_left(h,h1[i])
        ind -= 1
        if ind<0:
            ans.append(-1)
        elif sw[ind][0]<w1[i]:
            ans.append(sw[ind][1]+1)
        else:
            ans.append(-1)
        if ans[-1]==-1:
            ind = bisect.bisect_left(h, w1[i])
            ind -=1
            if ind<0:
                continue
            elif sw[ind][0]<h1[i]:
                ans.pop()
                ans.append(sw[ind][1]+1)
    print(*ans)