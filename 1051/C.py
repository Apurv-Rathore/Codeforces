n = int(input())
S = list(map(int, input().split()))
from collections import Counter, defaultdict
C = defaultdict(lambda: [])
for i, s in enumerate(S):
    C[s].append(i)
cnt = 0
X = []
Y = []
Z = []
for s, l in C.items():
    if len(l) == 2:
        X.append(l)
    elif len(l) == 1:
        Z.append(l)
        cnt += 1
    else:
        Y.append(l)
        cnt += 1
if cnt%2 == 0:
    ans = [0]*n
    Y = Y+Z
    for i, l in enumerate(Y):
        if i%2 == 0:
            for j in range(len(l)):
                if j == 0:
                    ans[l[j]] = 'A'
                else:
                    ans[l[j]] = 'B'
        else:
            for j in range(len(l)):
                if j == 0:
                    ans[l[j]] = 'B'
                else:
                    ans[l[j]] = 'A'
    for l in X:
        ans[l[0]] = 'A'
        ans[l[1]] = 'B'
    print('YES')
    print(''.join(ans))
else:
    if not Z:
        print('YES')
        print('A'*n)
        exit()
    ans = [0]*n
    if len(Z)%2 == 0:
        for i, l in enumerate(Z):
            if i%2 == 0:
                ans[l[0]] = 'A'
            else:
                ans[l[0]] = 'B'
        for i in range(n):
            if ans[i] == 0:
                ans[i] = 'A'
        print('YES')
        print(''.join(ans))
    else:
        if Y:
            for i, l in enumerate(Z):
                if i%2 == 0:
                    ans[l[0]] = 'A'
                else:
                    ans[l[0]] = 'B'
            for i in range(n):
                if ans[i] == 0:
                    ans[i] = 'A'
            l = Y[0]
            ans[l[0]] = 'B'
            for i in range(n):
                if ans[i] == 0:
                    ans[i] = 'A'
            print('YES')
            print(''.join(ans))
        else:
            print('NO')
