import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def printArr(arr):
	sys.stdout.write(" ".join(map(str,arr)) + "\n")

# Solution
def findNoOfWays(n):
	# Total no of ways in which two identical items (two knights) can be placed on n**2 places
	totalWays = (n**2)*((n**2)-1)//2

	# Total no of 2*3 regions = (n-1)*(n-2)  Total no of 3*2 regions = (n-1)*(n-2) 
	# Total no of ways two knights can be places per region so that they attack each others = 2
	noOfAttacks = 2*2*(n-1)*(n-2)

	# No of ways they do not attack each others = totalWays - noOfAttacks
	return totalWays-noOfAttacks

def solve(n):
	for i in range(1,n+1):
		answer = findNoOfWays(i)
		sys.stdout.write(str(answer) + "\n")

t=1
while t>0:
	n=int(input().decode())
	solve(n)
	t-=1
