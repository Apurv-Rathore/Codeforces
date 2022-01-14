# A Better (than Naive) Solution to find all divisiors 
import math 

# method to print the divisors 
def printDivisors(n) : 
	l=[]
	# Note that this loop runs till square root 
	i = 1
	while i <= math.sqrt(n): 
		
		if (n % i == 0) : 
			
			# If divisors are equal, print only one 
			if (n / i == i) : 
				l.append(int(i))
			else : 
				# Otherwise print both 
				l.append(i)
				l.append(int(n/i))
		i = i + 1
	return l
# Driver method 

#This code is contributed by Nikita Tiwari. 

t = int(input())
for _ in range(t):
    
    n,k = [int(x) for x in input().split()]
    if k>=n:
        print(1)
    else:
        l = printDivisors(n)
        l.sort()
        l.reverse()
        for i in range(len(l)):
            if l[i]<=k:
                print(n//l[i])
                break
        
                
                
                
            
