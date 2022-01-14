for _ in range(int(input())):
    n,m  = [int(X) for X in input().split()];aaa = 0
    for i in range(n):
        x = input();aaa+=x.count('#')
    print(pow(2,aaa,int(1e9+7)) - (1 if aaa==n*m else 0))