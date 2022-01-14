from sys import stdin
input = stdin.buffer.readline

n, d, m = map(int, input().split())
*a, = map(int, input().split())
a.sort()
c = sum(i <= m for i in a)
pref = [a[c - 1]]
ans = 0
tmp = 0
for i in range(c - 2, -1, -1):
	#print(i)
	pref.append(pref[-1] + a[i])
#print(a, pref, c)
for k in range(1, n + 1):
	tmp += a[n - k]
	b = (k - 1) * d
	if n - k - b < 0 or n - k < c:
		break
	s = tmp
	if c and n - k - b:
		s += pref[min(c - 1, n - k - b - 1)]
	#print(b, b - (n - k - c), s)
	ans = max(ans, s)
print(max(ans, pref[-1]))
