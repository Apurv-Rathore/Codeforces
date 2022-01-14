import sys
import math as mt
import bisect
#input=sys.stdin.buffer.readline  
#t=int(input())
t=1
for __ in range(t):
    #n=int(input())
    n,m,x,y=map(int,input().split())
    #l=list(map(int,input().split()))
    l=[]

    for i in range(n):
        l.append(input())
    yhash=[0]*(m+1)
    ydot=[0]*(m+1)
    j1=1
    for j in range(m):
        cnt=0
        for i in range(n):
            if  l[i][j]=='#':
                cnt+=1
        yhash[j1]=(cnt+yhash[j1-1])
        ydot[j1]=(n-cnt+ydot[j1-1])
        j1+=1
    dp=[[0 for i in range(m+1)]for j in range(2)]
    #dp[1][1]=1
    #print(dp)
    #print(yhash,ydot)
    for i in range(1,m+1):
        mini=10**6
        
        for j in range(x,y+1):
            if i-j>=0:
      #          print(i,i-j)
                mini=min(dp[0][i-j]+yhash[i]-yhash[i-j],mini)
        dp[1][i]=mini
    
        mini=10**6
        for j in range(x,y+1):
            if i-j>=0:
                mini=min(dp[1][i-j]+ydot[i]-ydot[i-j],mini)
        dp[0][i]=mini
    #print(dp)    
    print(min(dp[0][m],dp[1][m]))    
        