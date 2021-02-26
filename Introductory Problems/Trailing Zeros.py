import io,sys,os,math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
def printArr(arr):
	sys.stdout.write(" ".join(map(str,arr)) + "\n")
 
 
 
def solve(n):
	i=5
	count=0
	while i<=n:
		x= n//i
		i*=5
		count+=x
	return count
 
 
t=1
while t>0:
	n=int(input().decode())
	answer=solve(n)
	sys.stdout.write(str(answer)+'\n')
