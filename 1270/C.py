t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(j) for j in input().split()]
    x = 0
    for i in l:
        x^=i
    print(2)
    print(x+sum(l))
    print(x)