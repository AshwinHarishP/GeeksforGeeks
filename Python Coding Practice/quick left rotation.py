class Solution:
    def leftRotate(self, arr, k, n):
        rotations = k % n
        
        first_part = arr[rotations:]
        second_part = arr[:rotations]
        
        arr[:] = first_part + second_part
        return arr
        
        
        


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends
