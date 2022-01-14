n,m = [int(x) for x in input().split()]
l = []
for i in range(m):
    t = [int(x) for x in input().split()]
    l.append(t)

flag = 0
a,b = l[0]
tempa = []
tempb = []
for i in range(len(l)):
    if (a not in l[i]):
        tempa.append(l[i])
    if (b not in l[i]):
        tempb.append(l[i])

flag = 0
if (tempa==[]):
    print("YES")
    flag = 1
else:
    c,d = tempa[0]
    f = 0
    for i in range(len(tempa)):
        if (c not in tempa[i]):
            f = 1 
    if (f==0):
        print("YES")
        flag = 1
    if (flag==0):
        f = 0
        for i in range(len(tempa)):
            if (d not in tempa[i]):
                f = 1 
        if (f==0):
            print("YES")
            flag = 1

                
if (tempb==[] and flag==0):
    print("YES")
    flag = 1 
elif (flag==0):
    c,d = tempb[0]
    f = 0
    for i in range(len(tempb)):
        if (c not in tempb[i]):
            f = 1 
    if (f==0):
        print("YES")
        flag = 1
    if (flag==0):
        f = 0
        for i in range(len(tempb)):
            if (d not in tempb[i]):
                f = 1 
        if (f==0):
            print("YES")
            flag = 1

if (flag==0):
    print("NO")