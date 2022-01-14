import string
def function(l,r,k):
    length = r-l-1
    if length<2*k+1:
        return 0
    else:
        ans = (length-k)//(k+1)
        if ans>=0:
            return ans
        else:
            return 0
        
def function2(r,k):
    length = r-1
    ans = (length)//(k+1)
    if ans>=0:
        return ans
    else:
        return 0
    
def function3(l,k,n):
    length = n-l
    ans = (length)//(k+1)
    if ans>=0:
        return ans
    else:
        return 0
t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    abc = n
    s = input()
    index = []
    count=0
    if s.count('0')==len(s):
        length = len(s)
        length = length+k
        ans = length//(k+1)
        count+=ans
        print(count)
        continue
    for i in range(n):
        if s[i]=='1':
            index.append(i+1)
    for i in range(1,len(index)):
        count += function(index[i-1],index[i],k)
    if index:    
        a = index[0]
        b = index[-1]
        
        
        if a!=1:
            count+=function2(a,k)
        if b!=n:
            count+=function3(b,k,abc)
    
    print(count)
        
    