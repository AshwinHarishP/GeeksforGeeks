#User function Template for python3


class Solution:
    def missingNumber(self, array, n):
        # Calculate the expected sum of numbers from 1 to n
        expected_sum = (n * (n + 1)) // 2

        # Calculate the actual sum of the given array
        actual_sum = sum(array)

        # The missing number is the difference between the expected sum and the actual sum
        missing_number = expected_sum - actual_sum

        return missing_number

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends
