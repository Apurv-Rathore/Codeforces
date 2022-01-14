from sys import stdin
for _ in range (int(input())):
    n = int(input())
    r = [int(i) for i in list(input())]
    b = [int(i) for i in list(input())]
    x=0; y=0
    for i in range (n):
        if r[i]>b[i]:
            x+=1
        elif r[i]<b[i]:
            y+=1
    if x>y:
        print("RED")
    elif y>x:
        print("BLUE")
    else:
        print("EQUAL")