t = int(input())
for _ in range(t):
    n= int(input())
    summ=0
    for i in range(3,n+1):
        if i%2==1:
            summ = summ + (i-1)**2
    summ = summ*2
    print(summ)
