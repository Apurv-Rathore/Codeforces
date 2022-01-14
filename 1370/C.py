from math import ceil,log
t = int(input())
for _ in range(t):
    n = int(input())
    if (n==1):
        print("FastestFinger")
    elif (n==2 or n==3 or n%2==1):
        print("Ashishgup")
    elif (log(n,2)==int(log(n,2))):
        print("FastestFinger")
    else:
        if (n//4!=n/4):
            n//=2
            primes = []
            i = 3
            N = n*2
            while(i*i<=N):
                if (n%i==0):
                    
                    while(n%i==0):
                        primes.append(i)
                        primes.append(n//i)
                        n//=i
                i+=1
            if (len(primes)>1):
                print("Ashishgup")
            else:
                print("FastestFinger")
        else:
            print("Ashishgup")