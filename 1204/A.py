import sys,os,io
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
# else:
#     input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
t = 1
# t = int(input())
for _ in range(t):
    # n = int(input())
    # l = [int(x) for x in input().split()]
    s = input()
    y = len(s)-1
    ans = y//2
    if y%2==1 or s.count('1')>1:
        ans+=1
    print(ans)

