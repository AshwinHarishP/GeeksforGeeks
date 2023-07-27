class Solution:
    def countPairs(self, arr1, arr2, M, N, x):
        count = 0
        i = 0
        j = N - 1

        while i < M and j >= 0:
            current_sum = arr1[i] + arr2[j]
            if current_sum == x:
                count += 1
                i += 1
                j -= 1
            elif current_sum < x:
                i += 1
            else:
                j -= 1

        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    m,n=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=int(input())
    ob = Solution()
    print(ob.countPairs(a,b,m,n,x))


# } Driver Code Ends
