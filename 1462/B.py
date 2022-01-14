from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    ss = input()
    if (ss=='2020'):
        print("YES")
        continue
    l = list(ss)
    if (list("2020")==l[:4] or list("2020")==l[-4:] or (list("2020")==l[:1]+l[-3:]) or (list("2020")==l[:2]+l[-2:]) or (list("2020")==l[:3]+l[-1:])):
        print("YES")
    else:
        print("NO")
