from collections import deque
class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		n, m = len(grid), len(grid[0])
		visi = [[0] * m for _ in range(n)]
		dist = [[0] * m for _ in range(n)]
		
		Q = deque()
		
		for i in range(n):
		    for j in range(m):
		        if grid[i][j] == 1:
		            visi[i][j] = 1
		            dist[i][j] = 0
		            Q.append((i, j, 0))  
		          
        
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        
        while Q:
            
            r, c, d = Q.popleft()
            dist[r][c] = d
            
            for i in range(4):
                dr = r + delrow[i]
                dc = c + delcol[i]
                
                if 0 <= dr < n and 0 <= dc < m and visi[dr][dc] == 0:
                    visi[dr][dc] = 1
                    Q.append((dr, dc, d+1))
                    
        return dist
            
        

#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends
