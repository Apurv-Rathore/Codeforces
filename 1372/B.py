import math
def primeFactors(n): 
    l = []
    # Print the number of two\'s that divide n 
    while n % 2 == 0: 
        l.append(2) 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            l.append(int(i))
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        l.append(int(n))
    return l

t = int(input())
for _ in range(t):
    n = int(input())
    if n%2==0:
        print(n//2,n//2)
    else:
        x = primeFactors(n)
        min_lcm = 1000000000000000000
        pair = []
        for i in x:
            a = n//i
            b = n-a
            curr = max(a,b)
            if curr<min_lcm:
                min_lcm = curr
                pair = [a,b]
        print(*pair)









































#t = int(input())
#for _ in range(t):
#    n = int(input())
#    a = list(map(int,input().split()))
#    l1 = a[:]
#    l.sort()
#    if a==l:
#        print(0)
##    left_sorted = True
##    right_sorted = True
#    array = []
#    for i in range(n):
#        if i+1==a[i]:
#            array.append(1)
#        else:
#            array.append(0)
#    
#        