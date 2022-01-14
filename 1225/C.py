n,p = [int(x) for x in input().split()]
from math import log 
f = 0
def check(x,i):
    t = list(bin(x))[2:]
    if (t.count('1')<=i):
        return True
    return False
    
i  = 0
for i in range(0,100):
    
    if check((n-i*p),i) and n-i*p>=i:
        print(i)
        f = 1
        break
    
if (f==0):
    print(-1)