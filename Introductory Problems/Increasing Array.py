import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
#Solution
def solve(arr,n):
	moves=0
	for i in range(1,n):
		diff = arr[i]-arr[i-1]
		if diff<0:
			arr[i]=arr[i-1]
			moves+=abs(diff)
	return moves
 
t=1
while t>0:
	n=int(input().decode())
	arr=[int(i) for i in input().decode().strip().split()]
	answer=solve(arr,n)
	sys.stdout.write(str(answer)+'\n')
	t-=1
