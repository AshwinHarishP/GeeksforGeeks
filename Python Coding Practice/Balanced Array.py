#User function Template for python3

class Solution:
    def minValueToBalance(self,a,n):
        
        #Dividing array into 2 parts
        sub_array = len(a)//2
        
        #Adding elements of first sub array
        left_sum = 0
        for left_elements in range(sub_array):
            left_sum += a[left_elements]
            
        #Adding elements of right sub array
        right_sum = 0
        for right_element in range(sub_array,n):
            right_sum += a[right_element]
            
        balance = abs(left_sum - right_sum)
        
        return balance
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3





t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# } Driver Code Ends
