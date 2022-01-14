import sys
from collections import defaultdict, Counter

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)

# print(g)
rhomb = defaultdict(list)
for vert in g.keys():
    # print(0, vert)
    for neigh in g.get(vert, []):
        # print(1, neigh)
        for nexneigh in g.get(neigh, []):
            # print(2, nexneigh)
            if nexneigh == vert:
                continue
            rhomb[nexneigh].append(vert)
# print(rhomb)
ans = 0
for arr in rhomb.values():
    c = Counter(arr)
    for el in c:
        ans += (c[el]*(c[el]-1))//2

print(ans)
