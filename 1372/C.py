def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    l = a[:]
    l.sort()
    if a==l:
        print(0)
        continue
#    left_sorted = True
#    right_sorted = True
    array = []
    shit = [2]
    for i in range(n):
        if i+1==a[i]:
            if shit[-1]!=1:
                shit.append(1)
            array.append(1)
        else:
            if shit[-1]!=0:
                shit.append(0)
            array.append(0)
    shit = shit[1:]
    if shit==[1,0,1] or shit==[1,0] or shit== [0,1] or shit ==[0]:
        print(1)
    else:
        print(2)
    
        