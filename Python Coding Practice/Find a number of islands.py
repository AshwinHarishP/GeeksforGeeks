#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        
        def bfs(row, col, visited, grid):
            visited[row][col] = 1
            queue = [[row, col]]
            
            while queue:
                r = queue[0][0]
                c = queue[0][1]
                queue.pop(0)
                
                for delrow in range(-1, 2):
                    for delcol in range(-1, 2):
                        n_row = r + delrow
                        n_col = c + delcol
                        
                        if (n_row >= 0 and n_row < len(grid) and 
                           n_col >= 0 and n_col < len(grid[0]) and 
                           grid[n_row][n_col] == 1 and visited[n_row][n_col] != 1):
                               visited[n_row][n_col] = 1
                               queue.append([n_row, n_col])
            
            
        n, m = len(grid), len(grid[0])
        
        visited = [[0 for _ in range(m)]for _ in range(n)]
        cnt = 0
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and visited[row][col] == 0:
                    cnt += 1
                    bfs(row, col, visited, grid)
                    
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
