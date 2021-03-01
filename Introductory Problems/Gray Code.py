import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def printArr(arr):
    for i in arr:
        sys.stdout.write(i+ "\n")

#solution
def solve(n):
    result=list()
    i = 2 
    result.append('0')
    result.append('1')
    while i<2**n:
        for j in range(len(result)-1,-1,-1):
            result.append(result[j])
        x=len(result)
        for j in range(i):
            result[j]='0'+result[j]
        for j in range(i,x):
            result[j]='1'+result[j]
        i*=2
    return result
		



t=1
while t>0:
	n=int(input().decode())
	answer=solve(n)
	printArr(answer)
	t-=1

