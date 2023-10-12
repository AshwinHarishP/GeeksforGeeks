#User function Template for python3

class Solution:
    def jugglerSequence(self, N):
        if N == 1:
            return [N]
            
        if N % 2 == 0:
            next_term = int(N ** 0.5)
        else:
            next_term = int(N ** 1.5)
            
        return [N] + self.jugglerSequence(next_term)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.jugglerSequence(N)
        for i in (arr):
            print(i,end=" ")
        print()
# } Driver Code Ends
