N, K = [int(x) for x in input().split(' ')]
f = list(range(N))
def find(x):
    if x != f[x]:
        f[x] = find(f[x])
    return f[x]
res = 0
for _ in range(K):
    a, b = [int(x)-1 for x in input().split(' ')]
    fa, fb = find(a), find(b)
    if fa != fb:
        res += 1
        f[fa] = fb
print(K-res)