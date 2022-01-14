import string
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    list_s = list(s)
    l=list_s
    if set(l)=={'1'} or set(l)=={'0'}:
        print(s)
    else:
            
        s_reverse = list_s[:]
        s_reverse.reverse()
        last_0 = s_reverse.index('0')
        last_0 = n-last_0-1
        first_1 = list_s.index('1')
        ans=[]
        if last_0+1==first_1:
            print(s)
        else:
            first_0=list_s.index('0')
            last_1 = n-s_reverse.index('1')-1
            if first_0==last_1+1:
                print(0)
            else:
                ans=[]
                s = list_s
                ans = ans+s[:first_1]
                ans = ans+ s[last_0:]
                a=''
                for i in ans:
                    a+=i
                print(a)
        