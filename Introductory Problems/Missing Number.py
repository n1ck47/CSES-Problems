import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def printArr(arr):
	sys.stdout.write(" ".join(map(str,arr)) + "\n")

# Solution
def solve(arr,n):
	freq = [0 for i in range(n+1)]
	for elm in arr:
		freq[elm] = 1
	for i in range(1,n+1):
		if freq[i]==0:
			return i

t=1
while t>0:
	n=int(input().decode())
	arr=[int(i) for i in input().decode().strip().split()]
	answer=solve(arr,n)
	sys.stdout.write(str(answer)+'\n')
	t-=1
