#User function Template for python3

class Solution:
    def find_multiplication (self, arr, brr, n, m) : 
        max_arr = max(arr)
        min_arr = min(brr)
        
        return max_arr * min_arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
    
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    m = int(input())
    brr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.find_multiplication(arr, brr, n, m)
    print(res)






# } Driver Code Ends
