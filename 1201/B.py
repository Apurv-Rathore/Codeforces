t = int(input())
l = [int(x) for x in input().split()]
if (sum(l))%2==0 and max(l)<=sum(l)-max(l):
    print("YES")
else:
    print("NO")