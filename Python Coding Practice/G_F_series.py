class Solution:
    
    def gfSeries(self, N : int) -> None:
        
        for i in range(1, N+1):
            print(self.func(i),end=" ")
        print()
        
        
    def func(self, N):
        if N < 1:
            return
        
        if N == 1:
            return 0
        
        if N == 2:
            return 1
            
        return self.func(N-2)**2 - self.func(N-1) 


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        obj = Solution()
        obj.gfSeries(N)

# } Driver Code Ends
