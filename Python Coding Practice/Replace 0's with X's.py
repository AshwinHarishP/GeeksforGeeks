#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        def dfs(row, col):
            visited[row][col] = 1
            
            for i in range(4):
                dr = row + delRow[i]
                dc = col + delCol[i]
                    
                if 0 <= dr < n and 0 <= dc < m and not visited[dr][dc] and mat[dr][dc] == "O":
                    dfs(dr, dc)
            
            
            
        visited = [[0] * m for _ in range(n)]
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]
        for j in range(m):
            
            if not visited[0][j] and mat[0][j] == "O":
                dfs(0, j)
                
            if not visited[n-1][j] and mat[n-1][j] == "O":
                dfs(n-1, j)
                
                
        for i in range(n):
            
            if not visited[i][0] and mat[i][0] == "O":
                dfs(i, 0)
                
            if not visited[i][m-1] and mat[i][m-1] == "O":
                dfs(i, m-1)
                
                
        for i in range(n):
            for j in range(m):
                if mat[i][j] == "O" and not visited[i][j]:
                    mat[i][j] = "X"
                    
        return mat

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends
