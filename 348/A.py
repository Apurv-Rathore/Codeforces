from math import ceil 
n = int(input())
l = [int(x) for x in input().split()]
x = (sum(l))
a = ceil(x/(n-1))
print(max(a,max(l)))