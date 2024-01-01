#User function Template for python3
import math
class Solution:
    def maxBinTreeGCD(self, arr, N):
        if len(arr) <= 1:
            return 0
            
        arr.sort()
            
        maxi = 0
        
        a = arr[0]
        for i in range(1, len(arr)):
            b = arr[i]
            
            if a[0] == b[0]:
                maxi= max(maxi, math.gcd(a[1], b[1]))
                
            a = b
        return maxi
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from math import gcd
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=[]
        
        for i in range(N-1):
            u,v=map(int,input().split())
            arr.append([u,v])
        
        ob = Solution()
        print(ob.maxBinTreeGCD(arr,N))
# } Driver Code Ends
