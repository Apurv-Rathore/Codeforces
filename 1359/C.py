def check(h,c,x,t):
    return abs((x*(h+c-2*t)+t-c)/(2*x-1))

def answer(h,c,t):
    avg=(h+c)//2
    if t<=avg:
        return 2
    x=(t-c)//(2*t-h-c)
    if check(h,c,x,t)<=check(h,c,x+1,t):
        return 2*x-1
    else:
        return 2*x+1             
t=int(input())
for i in range(t):
    h,c,t=map(int,input().split())
    print(answer(h,c,t))           