n,k = [int(j) for j in input().split()]
from collections import defaultdict
dic = defaultdict(lambda:0)
for i in range(k+1):
    l = [int(j) for j in range(1,k+2)]
    l.remove(i+1)
    print('?',*l)
    x,y = [int(j) for j in input().split()]
    dic[y]+=1
print("!",dic[max(dic)])