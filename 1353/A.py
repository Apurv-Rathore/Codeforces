t = int(input())
for _ in range(t):
    length , summ = [int(x) for x in input().split()]
    
    if length==1:
        print(0)
        continue
    if length%2==1:
        print(2*summ)
    else:
        if length==2:
            print(summ)
        else:
            print((2*summ))
        
    