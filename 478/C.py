l = [int(x) for x in input().split()]
l.sort()
a,b,c = l 
if (c<2*(a+b)):
    print((a+b+c)//3)
else:
    print(a+b)