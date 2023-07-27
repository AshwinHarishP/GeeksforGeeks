#User function Template for python3
from collections import Counter
class Solution:
	
	def findSum(self,arr, n):
		count_arr = Counter(arr)
		Sum = 0
		for keys,values in count_arr.items():
		    if values <= 1:
		       Sum += keys
		    else:
		        Sum += keys
		        del keys
	    return Sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
