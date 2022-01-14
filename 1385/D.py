import string
x = 'abcdefghijklmnopqrstuvwxyz'

def func(s,n,i):
    if len(s)==1:
        if s==x[i]:
            return 0
        else:
            return 1

    left_count = s[:n//2].count(x[i])
    right_count = s[n//2:].count(x[i])
#    print(s[:n//2],s[n//2:])
#    print(left_count,right_count)
#    if left_count>right_count:
        
#        return (func(s[n//2:],n//2,i+1) + (n//2-(left_count)))
#    if left_count<right_count:
#        return (func(s[:n//2],n//2,i+1) + (n//2-(right_count)))
#    if left_count==right_count:
    return min((func(s[:n//2],n//2,i+1) + (n//2-(right_count))),(func(s[n//2:],n//2,i+1) + (n//2-(left_count))))
    
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(func(s,n,0))
    