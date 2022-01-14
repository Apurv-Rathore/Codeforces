n = int(input())
l = list(map(int,input().split()))
b  = [0]*21; ans = 0
for i in l:
    x = bin(i)[2:][::-1]
    for j in range(len(x)):
        b[j]+=int(x[j])
while(1):
    f = 0; s = ''
    for i in range(20,-1,-1):
        if (b[i]>0):
            s+='1';b[i]-=1
        else:
            s+='0'
    ans+=int(s,2)*int(s,2)
    if (int(s,2)==0):
        break
print(ans)