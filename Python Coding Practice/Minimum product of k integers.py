#User function Template for python3

class Solution:
    def minProduct(self, a, n, k): 
        a = sorted(a)
        prod = 1
        for i in range(k):
            prod = (prod *a[i]) %(10**9+7)
            
        return prod
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    k = int(input())
    ob=Solution()
    print(ob.minProduct(arr, n, k))
    
# } Driver Code Ends
