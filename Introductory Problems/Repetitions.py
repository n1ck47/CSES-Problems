import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

#Solution
def solve(string,n):
	max_count=1
	count=1
	curr_letter=string[0]
	for i in range(1,n):
		if string[i]==curr_letter:
			count+=1
		else:
			max_count=max(count,max_count)
			count=1
			curr_letter=string[i]
	max_count=max(count,max_count)
	return max_count
t=1
while t>0:
	string=input()
	answer=solve(string,len(string))
	sys.stdout.write(str(answer)+'\n')
