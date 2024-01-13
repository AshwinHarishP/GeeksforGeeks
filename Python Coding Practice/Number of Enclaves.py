#User function Template for python3

from typing import List
from collections import deque
class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        
        q = deque()
        n, m = len(grid), len(grid[0])
        visited = [[0 for _ in range(m)]for _ in range(n)]
        
        delRows = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]
        # upper and lower Columns
        for j in range(m):
            if grid[0][j] == 1:
                q.append((0, j))
                
            if grid[n-1][j] == 1:
                q.append((n-1, j))
                
                
        # upper and lower rows
        for i in range(n):
            if grid[i][0] == 1:
                q.append((i, 0))
                
            if grid[i][m-1] == 1:
                q.append((i, m-1))
                
        while q:
            r, c = q.popleft()
            visited[r][c] = 1
            
            for k in range(4):
                nRow = r + delRows[k]
                nCol = c + delCol[k]
                
                if nRow >= 0 and nRow < n and nCol >= 0 and nCol < m and not visited[nRow][nCol] and grid[nRow][nCol] == 1:
                    q.append((nRow, nCol))
            
                
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    cnt += 1
        return cnt
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends
