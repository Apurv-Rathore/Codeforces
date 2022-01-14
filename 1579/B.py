# B
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    tmp=[]
    for i in range(n):
        min_n=min(arr)
        min_i=arr.index(min_n)
        if min_i: tmp.append([i+1,i+1+min_i,min_i])
        del arr[min_i]
    print(len(tmp))
    for i in tmp:
        print(*i)
