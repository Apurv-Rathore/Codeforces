def ffff(s,x,n):
    print(x+1,n,x+2,n)
def fff(n):
    print(2,n//2+1,1,n//2)
def ff(s,n):
    for i in range(n//2,n):
        if s[i]=='0':
            print(1,i+1,1,i)
            return True 
    return False 
for _ in range(int(input())):
    n = int(input())
    s = list(input())   
    if ff(s,n):
        continue 
    if '0' not in s:
        fff(n)
    else:
        x = s.index('0')
        ffff(s,x,n)
