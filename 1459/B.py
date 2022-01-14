from sys import stdin
n = int(input())
if n%2 == 1:
    print(int(1+(3*n*(n+4)+2-(-1)*(n*(n+4)+2))/8))
else:
    print(int(1+(3*n*(n+4)+2-(n*(n+4)+2))/8))