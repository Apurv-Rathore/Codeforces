for i in range(int(input())):
	n = int(input())
	a = [int(j) for j in input().split()]
	flag = True
	for i in range(len(a)-1):
		if abs(a[i+1]-a[i]) > 1 :
			print('YES')
			print(i+1,i+2)
			flag = False
			break
	if flag == True:
		print('NO')