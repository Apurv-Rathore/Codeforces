# for _ in range(1):
for _ in range(int(input())):
    n, k, zz = map(int, input().split())
    # n = int(input())
    arr = list(map(int, input().split()))
    # s = input()
    ans = 0
    for z in range(0, zz + 1):
        an = 0
        mx = 0
        for i in range(0, k - 2 * z + 1):
            an += arr[i]
            if i + 1 < n:
                mx = max(mx, arr[i] + arr[i + 1])
        an += z * mx
        ans = max(ans, an)
 
    print(ans)
 