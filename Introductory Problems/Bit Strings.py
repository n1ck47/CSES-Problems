import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
def printArr(arr):
	sys.stdout.write(" ".join(map(str,arr)) + "\n")
 
def solve(arr,n):
	pass
 
t=1
while t>0:
	n=int(input().decode())
	modulo = 10**9 + 7
	answer=(2**n)%modulo
	sys.stdout.write(str(answer)+'\n')
	t-=1
