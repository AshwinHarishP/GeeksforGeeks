#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        
        def dfs(i, j):
            visited[i][j] = 1
            for k in range(8):
                Nrow = i + dx[k]
                Ncol = j + dy[k]
                
                if Nrow >= 0 and Nrow < n and Ncol >= 0 and Ncol < m and not visited[Nrow][Ncol] and grid[Nrow][Ncol] == 1:
                    dfs(Nrow, Ncol)
                
                
            
        n, m = len(grid), len(grid[0])
        visited = [[0 for _ in range(m)]for _ in range(n)]
        dx= [-1,-1,-1,0,0, 1, 1, 1]
        dy = [-1,0, 1,-1, 1,-1,0, 1]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    cnt += 1
                    dfs(i, j)
        return cnt
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends
