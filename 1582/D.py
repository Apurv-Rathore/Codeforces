from math import *
def sign(num):return -1 if num < 0 else 1
for _ in range(int(input())):
	n = int(input());l = list(map(int, input().split()))
	if n % 2:
		a, b, c, *l = l
		print(abs(b) * sign(a), (abs(a) + abs(c)) * -sign(b), abs(b) * sign(c), end = ' ')
	for i in range(0, len(l), 2):print(abs(l[i + 1]) * -sign(l[i]), abs(l[i]) * sign(l[i + 1]), end = ' ')
	print()