#User function Template for python3
class Solution:
    def convertEvenBitToZero (ob, n):
        
        temp=n
        i=0
        while(n>0):
            temp=temp&~(1<<i)
            i+=2
            n=n>>2
        # code here 
        return temp

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.convertEvenBitToZero(n))
# } Driver Code Ends
