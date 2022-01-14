import os,io,sys

if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    if n%2==1:
        print("Bob")
        continue 
    cnt = 0
    n1 = n
    while(n1%2==0):
        cnt+=1
        n1//=2 
    if n1!=1:
        print("Alice")
    else:
        if cnt%2==0:
            print("Alice")
        else:
            print("Bob")




        

    
    

    # # print(d)
    # d.sort(reverse=True)
    # pos = [[1,1],[1,m],[n,m],[n,1]]
    # # print(d[0][1]-1,d[1][1]-1)
    # ans = pos[d[0][1]-1]+pos[d[1][1]-1]
    # print(*ans)
