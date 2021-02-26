import io,sys,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def printArr(arr):
	sys.stdout.write(" ".join(map(str,arr)) + "\n")

# Solution
def solve(arr,n):
	frequency = dict()
	for letter in arr:
		frequency[letter] = frequency.get(letter,0) + 1
	flag = False
	odd = None
	oddFreq = None
	palindrome=''
	for keys in frequency:
		if frequency[keys]%2==1:
			if flag:
				return 'NO SOLUTION'		# if there are more than one letter having a odd frequency
			flag = True
			odd = keys
			oddFreq = frequency[keys]
	if oddFreq:
		palindrome = odd*oddFreq
	for keys in frequency:
		freq = frequency[keys]
		if freq%2==0:
			front = keys*(freq//2)
			palindrome = front + palindrome + front
	return palindrome



t=1
while t>0:
	arr=[i for i in input().decode().strip()]
	answer=solve(arr,len(arr))
	sys.stdout.write(str(answer)+'\n')
	t-=1
