#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        def dfs(row, col, i, j):
            
            visited[row][col] = 1
            temp.append((row - i, col - j))
            
            for k in range(4):
                dr = row + delrow[k]
                dc = col + delcol[k]
                
                if dr >= 0 and dr < n and dc >= 0 and dc < m and not visited[dr][dc] and grid[dr][dc] == 1:
                    dfs(dr, dc, i, j)
            

            
        n, m = len(grid), len(grid[0])
        
        visited = [[0 for _ in range(m)]for _ in range(n)]
        islands = set()
        
        delrow = [-1, 0, 1, 0]
        delcol = [0, -1, 0, 1]

        for i in range(n):
            for j in range(m):
                temp = []
                if not visited[i][j] and grid[i][j] == 1:
                    dfs(i, j, i, j)
                    islands.add(tuple(temp))
        
        return len(islands)
