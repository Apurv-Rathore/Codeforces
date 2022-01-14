import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input()
    ans, count, total = 0, 0, 0
    for i in range(k):
        count = 0
        for j in range(i, n, k):
            if a[j] == "1":
                count += 1
                total += 1
            else:
                count -= 1
                if count < 0:
                    count = 0
            ans = max(ans, count)
    print(total - ans)
