t = int(input())
for _ in range(t):
    n = int(input())
    if n<=30:
        print("NO")
    else:
        if n>44 :
            print("YES")
            print(6,10,14,n-30)
        else:
            if n==36 or n==40 or n==44:
                print("YES")
                if n==36:
                    
                    print(5 ,6 ,10 ,15)
                elif n==40:
                    print(21,10,6,3)
                else:
                    print(15,6,10,13)
            else:
                print("YES")
                print(6,10,14,n-30)