import io,sys,os
sys.setrecursionlimit(10**9)
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
def printArr(arr):
	sys.stdout.write(" ".join(map(str,arr)) + "\n")
 
def solve(a,b):
	large=max(a,b)
	small=min(a,b)
	difference = large-small
	large = large - difference*2
	small = small - difference
	if large==0 and small==0:
		return True
	if small<=0:
		return False
	if large==small:
		if large%3==0 and small%3==0:
			return True
	return False
 
 
t=int(input().decode())
while t>0:
	arr=[int(i) for i in input().decode().strip().split()]
	a,b=arr[0],arr[1]
	answer=solve(a,b)
	if answer:
		answer='YES'
	else:
		answer='NO'
	sys.stdout.write(str(answer)+'\n')
	t-=1
