# n,m = [int(x) for x in stdin.readline().split()]
n,m = [int(x) for x in input().split()]
if m>(2*n+2):
    print(-1)
elif m<(n-1):
    print(-1)
elif m==(n-1):
    s='01'*(n-1)+'0'
    print(s)
else:
    if m==n:
        s='10'*n
        print(s)
    else:
        x=n+1
        y=m-x
        s='110'*y
        if y==(n+1):
            print('110'*n+'11')
        elif y==(n):
            print('110'*n+'1')
        else:
            print(s+'10'*(n-y)+'1')