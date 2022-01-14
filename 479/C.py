n = int(input())
l = []
for _ in range(n):
    l.append([int(x) for x in input().split()])
l.sort()
c = l[0][1]
for i in range(n):
    if (c<=l[i][1]):
        c =l[i][1]
    else:
        c = l[i][0]
print(c)