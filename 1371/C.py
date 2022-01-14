t = int(input())
for _  in range(t):
    a,b,m,n = map(int,input().split())
    if a+b<m+n:
        print("No")
        continue

    minimum = min(a,b)
    maximum = max(a,b)
    if minimum>=n:
        if a+b-n>=m:
            print("Yes")
        else:
            print("No")
    elif a==b:
        if a>=n:
            if a+b-n>=m:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
        
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
#    else:
#        
#        if a>b:
#            if m-(a-b)>=0:
#                m -=a-b
#            else:
#                print("No")
#                continue
#        elif a<b:
#            if m+(a-b)>=0:
#                m +=a-b
#            else:
#                print("No")
#                continue
#        
#        
#        
#        
#        
#        ans  =True
#        
#        
#        if a==b:
#            if m==n:
#                print("Yes")
#            elif m>n:
#                if m>=a-b+n:
#                    print("Yes")
#                else:
#                    print("No")
#            else:
#                if m%2==0:
#                    if a-(m//2)>=n:
#                        print("Yes")    
#                    else:
#                        print("No")
#                else:
#                    if a-(m//2)-1>=n:
#                        print("Yes")    
#                    else:
#                        print("No")
#    