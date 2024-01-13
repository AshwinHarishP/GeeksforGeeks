#User function Template for python3

import sys
from typing import List
from collections import deque
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        def bfs(row, col, i, j):
            Q.append((row, col))
            visited[row][col] = 1
            temp.append((row - i, col - j))
            
            while Q:
                row, col = Q.popleft()
                
                for k in range(4):
                    n_row = row + delRow[k]
                    n_col = col + delCol[k]
                    
                    if n_row >= 0 and n_row < n and n_col >= 0 and n_col < m and grid[n_row][n_col] == 1 and not visited[n_row][n_col]:
                        bfs(n_row, n_col, i, j)
                
        
        Q = deque()
        visited = [[0 for _ in range(m)]for _ in range(n)]
        islands = set()
        delRow = [-1, 0, 1, 0]
        delCol = [0, -1, 0, 1]
        
        for i in range(n):
            for j in range(m):
                temp = []
                if not visited[i][j] and grid[i][j] == 1:
                    bfs(i, j, i, j)
                    islands.add(tuple(temp))
                    
        return len(islands)
        


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
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends
