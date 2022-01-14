p,d=map(int,input().split())
s=0
if p<10:
    print(p)
else:
    i=10
    while i<=p:
        if (p%i)+1<=d and (p%i)+1!=i:
            s=(p%i)+1
            i=i*10
        else:
            i=i*10
    print(p-s)