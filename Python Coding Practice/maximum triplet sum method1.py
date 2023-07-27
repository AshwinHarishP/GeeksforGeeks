#User function Template for python3

class Solution:
    def maxTripletSum (self, arr,  n) : 
        first = second = third = float('-inf')

        for i in range(n):
            if arr[i] > first:
                third = second
                second = first
                first = arr[i]
            elif arr[i] > second:
                third = second
                second = arr[i]
            elif arr[i] > third:
                third = arr[i]
    
        return first + second + third



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
