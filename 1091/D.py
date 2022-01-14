fact = [0] * 1000001
fact[0] = 1
mod = 998244353
n = int(input())
fact[n] = n
for i in range(n - 1, -1, -1):
    fact[i] = (fact[i + 1] * i) % mod
ans = (n * fact[1]) % mod
for i in range(1, n):
    ans = (ans + mod - fact[n - (n - i) + 1]) % mod
print(int(ans))