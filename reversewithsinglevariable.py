start=0
end=0
def reverseList(A):
  global start,end
	if start >= end:
		return
	A[start], A[end] = A[end], A[start]
  start+=1
  end-=1
	reverseList(A)


A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A)
print("Reversed list is")
print(A)

