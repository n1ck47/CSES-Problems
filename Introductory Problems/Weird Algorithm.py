import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def printArr(arr):
	sys.stdout.write(" ".join(map(str,arr)) + "\n")

# Solution 
def solve(n):
	while True:
		sys.stdout.write(str(n)+' ')
		if n==1:
			break
		if n%2==0:
			n=n//2
		else:
			n = n*3 +1

t=1
while t>0:
	n=int(input().decode())
	solve(n)
	t-=1
