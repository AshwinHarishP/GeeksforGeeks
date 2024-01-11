#User function Template for python3

class Solution:
    def numProvinces(self, adj, v):
        
        def dfs(node, visited, adjLs):
            
            visited[node] = 1
            for i in adjLs[node]:
                if visited[i] == 0:
                    dfs(i, visited, adjLs)
            
            
            
        adjLs = [[] for _ in range(v)]
        visited = [0] * v
        
        for i in range(v):
            for j in range(v):
                if adj[i][j] == 1:
                    adjLs[i].append(j)
                    adjLs[j].append(i)
                    
        cnt = 0
        for i in range(v):
            if not visited[i]:
                cnt += 1
                dfs(i, visited, adjLs)
                
        return cnt
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends
