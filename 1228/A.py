from sys import stdin
# t = int(input())
def check (n):
    n = list(str(n))
    if (len(set(n))==len(n)):
        return True 
    return False
t = 1
for _ in range(t):
    # n = int(input())
    l,r = [int(x) for x in stdin.readline().split()]
    f = 0
    for i in range(l,r+1):
        if (check(i)):
            print(i)
            f = 1
            break
    if (f==0):
        print(-1)
    