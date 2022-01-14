a, b = map(int, input().split())
if b>9*a or (b == 0 and a != 1):print(-1, -1)
elif a == 1 and b == 0:print(0, 0)
else:
    M, m = 0, 10**(a-1)
    for i in range(b-1):m += 10 ** (i//9)
    for i in range(b):M += 10 ** (a-1-i//9)
    print(m, M)