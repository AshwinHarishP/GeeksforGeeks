#User function Template for python3

from typing import List
from queue import deque
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        def isValid(newr, newc, n, m):
            if newr >= 0 and newr < n and newc >= 0 and newc < m:
                return True
            return False
            
            
        if source == destination:
            return 0
            
        n, m = len(grid), len(grid[0])
        dist = [[float("inf") for _ in range(m)] for _ in range(n)]
        Q = deque()
        
        dist[source[0]][source[1]] = 0
        Q.append((0, source[0], source[1] ))
        
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        
        while Q:
            dis, r, c = Q.popleft()
            
            for i in range(4):
                newr = r + dr[i]
                newc = c + dc[i]
                
                if isValid(newr, newc, n, m) and grid[newr][newc] == 1 and dis + 1 < dist[newr][newc]:
                    if [newr, newc] == destination:
                        return dis + 1
                        
                    dist[newr][newc] = dis + 1
                    Q.append((dis + 1, newr, newc))
        return -1
            
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends
