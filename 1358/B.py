
t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    i=n-1
    flag=0
    while i>=0:
        if l[i]<=i+1:
            print(i+2)
            flag=1
            break
        i-=1
    if flag==0:
        print(1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#    l.sort()
#    dic = defaultdict(lambda :0)
#    for i in range(n):
#        dic[l[i]] +=1
#    count=1
#    women=0
#    l = list(set(l))
#    for i in range(len(set(l))):
#        print(dic[l[i]])
#        print(women)
#        
#        if l[i]<=women+dic[l[i]]:
#            women +=dic[l[i]]
#    print(women+1)