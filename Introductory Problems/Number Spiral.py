import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
def printArr(arr):
	for i in arr:
		sys.stdout.write(str(i)+' ')
	sys.stdout.write('\n')
 
#Solution
def solve(arr):
	row=arr[0]
	column=arr[1]
	size = max(row,column)
	answerIndex = column + size-row
	if size%2==1:
		startPoint = (size-1)*(size-1) +1
		answer = startPoint + answerIndex -1
	else:
		startPoint = size*size
		answer = startPoint - answerIndex +1
	return answer
 
 
t=int(input().decode())
while t>0:
	arr=[int(i) for i in input().decode().strip().split()]
	answer=solve(arr)
	sys.stdout.write(str(answer)+'\n')
	t-=1
