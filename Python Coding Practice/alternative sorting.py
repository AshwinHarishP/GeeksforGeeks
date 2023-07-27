class Solution:
    def alternateSort(self,arr, N):
        List = []
        arr = sorted(arr,reverse = True)
        
        for i in range(N//2):
            List.append(arr[i])
            List.append(arr[-i-1])
            
        if N % 2 != 0:
            List.append(arr[N//2])
        arr[:] = List
        return arr

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    def printAns(ans):
        for x in ans:
            print(x, end=" ");
        print()
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        obj=Solution()
        ans=obj.alternateSort(a,n)
        printAns(ans)
# } Driver Code Ends
