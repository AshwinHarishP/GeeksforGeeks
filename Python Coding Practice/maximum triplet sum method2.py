#User function Template for python3

class Solution:
    def maxTripletSum(self, arr, n):
        max_sum = float('-inf')
    
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    triplet_sum = arr[i] + arr[j] + arr[k]
                    max_sum = max(max_sum, triplet_sum)

        return max_sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.maxTripletSum(arr, n)
    print(res)



# } Driver Code Ends
