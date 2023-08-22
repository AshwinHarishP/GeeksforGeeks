#User function Template for python3
class Solution:

	
	def search(self,arr, n, k): 
    	for i in range(n):
    	    
    	    if arr[i] == k:  #Checking element matches k
    	        return i+1      #incrementing the index by 1 as it is 1 based indexing     
    	return -1       #No result found



#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, k=map(int, input().strip().split())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.search(arr, n, k)
        print(ans)
        tc=tc-1
# } Driver Code Ends
