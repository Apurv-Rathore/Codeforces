
mod = 998244353 
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime
tt= int(input())
prime = SieveOfEratosthenes(1000000)
for _ in range(tt):
    pre=  1
    ans = 1
    n = int(input())
    c = 2
    while(c<4):
        for i in range(2,len(prime)):
            if (i-pre>=n):
                if (prime[i]==True):
                    ans*=i
                    c+=1
                    pre = i
                if (c==4):
                    break
    print(ans)
