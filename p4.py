
def numofsubset(arr, n):


x = sorted(arr)

count = 1

for i in range(0, n-1):

	
	if (x[i] + 1 != x[i + 1]):
	count = count + 1

return count

t=int(input())
arr=list(map(int,input().split()))
n = len(arr)
print numofsubset(arr, n)

# This code is contributed by Afzal Ansari.
