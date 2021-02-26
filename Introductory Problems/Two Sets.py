import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
def printArr(arr):
	sys.stdout.write(" ".join(map(str,arr)) + "\n")
 
# Solution
def solve(n):
	totalSum = n*(n+1)//2
	if totalSum%2==0:
		s1,s2=[],[]
		front,rear = 1,n
		sumSet1=0
		if n%4==3:
			s1 = [1,2]
			s2 = [3]
			front = 4
			sumSet1 = 3
		while sumSet1!=totalSum//2:
			s1.append(front)
			s1.append(rear)
			sumSet1+= front+rear
			front+=1
			rear-=1
		temp = [i for i in range(front,rear+1)]
		s2.extend(temp)
		sys.stdout.write('YES'+'\n')
		sys.stdout.write(str(len(s1))+'\n')
		printArr(s1)
		sys.stdout.write(str(len(s2))+'\n')
		printArr(s2)
	else:
		sys.stdout.write('NO'+'\n')
 
t=1
while t>0:
	n=int(input().decode())
	solve(n)
	t-=1
