class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    
	    def dfs(row, col, new_board):
	        new_board[row][col] = newColor
	        for i in range(4):
	            nrow = row + delRow[i]
	            ncol = col + delCol[i]
	            if nrow >= 0 and nrow < len(image) and ncol >= 0 and ncol < len(image[0]) and image[nrow][ncol] == ini_color and new_board[nrow][ncol] != newColor:
	                dfs(nrow, ncol, new_board)
	       
	    
	    new_board = image
		ini_color = new_board[sr][sc]
		delRow = [-1, 0, 1, 0]
		delCol = [0, 1, 0, -1]
		
		dfs(sr, sc, new_board)
		return new_board
		
		
		



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)


T=int(input())
for i in range(T):
	n, m = input().split()
	n = int(n)
	m = int(m)
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))
	sr, sc, newColor = input().split()
	sr = int(sr); sc = int(sc); newColor = int(newColor);
	obj = Solution()
	ans = obj.floodFill(image, sr, sc, newColor)
	for _ in ans:
		for __ in _:
			print(__, end = " ")
		print()
# } Driver Code Ends
