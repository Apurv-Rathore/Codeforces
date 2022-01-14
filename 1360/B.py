t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    minimum=100000000
    x=[]
    for i in range(n-1):
        diff = l[i+1]-l[i]

        x.append(diff)
    print(min(x))
#        if l[i+1]-l[i]<minimum:
#            print(l[i+1]-l[i])
#            minumim = l[i+1]-l[i]
#    print(minimum)
#        