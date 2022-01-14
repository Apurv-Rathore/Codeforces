import sys

#comment these out later
#sys.stdin = open("in.in", "r")
#sys.stdout = open("out.out", "w")

input = sys.stdin.readline

def main():
	t = int(input())
	#t = 1

	for _ in range(t):

		def swap(k):
			for i, x in enumerate(inds):
				if x <= k:
					inds[i] = k-x+1

			ans.append(k)

		n = int(input())
		ar = list(map(int, input().split()))

		cycs = (n-1)//2

		ans = []

		bad = False

		inds = [0]*n

		for i, x in enumerate(ar):
			if x%2 == i%2:
				print(-1)
				bad = True
				break
			inds[x-1] = i+1

		if bad:
			continue

		for x in range(cycs):
			a = n - 2*x
			b = a - 1

			aind = inds[a-1]
			bind = inds[a-2]

			#print(a, b, aind, bind)

			swap(inds[a-1])
			swap(inds[a-2] - 1)
			swap(inds[a-2] + 1)
			swap(3)
			swap(a)

		print(5*cycs)

		print(*ans)


main()