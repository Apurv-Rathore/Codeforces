hm = int(input())
while hm>0:
	hm-=1

	n = int(input())
	s = (input()).split()
	a = []
	for i in s:
		a.append(int(i))

	l = 0
	while l < n:
		if a[l] < l:
			break
		l += 1

	r = n-1
	while r >= 0:
		if a[r]<(n-r-1):
			break
		r -= 1

	l -= 1
	r += 1
	if l >= r:
		print("Yes")
	else:
		print("No")
