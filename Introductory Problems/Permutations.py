import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
def printArr(arr):
	for i in arr:
		sys.stdout.write(str(i)+' ')
	sys.stdout.write('\n')
 
#Solution
def solve(arr,n):
	answer=list()
	for i in range(1,n,2):
		answer.append(arr[i])
	for i in range(0,n,2):
		answer.append(arr[i])
	return answer
 
t=1
while t>0:
	n=int(input().decode())
	if n==3 or n==2:
		sys.stdout.write('NO SOLUTION')
		break
	arr=[int(i) for i in range(1,n+1)]
	answer=solve(arr,n)
	printArr(answer)
	t-=1
