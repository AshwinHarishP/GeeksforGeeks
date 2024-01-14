#User function Template for python3

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        def dfs(node):
            visited[node] = 1
            path[node] = 1
            check[node] = 0
            
            for i in adj[node]:
                if not visited[i]:
                    if dfs(i):
                        check[node] = 0
                        return True
                    
                elif path[i]:
                    check[node] = 0
                    return True
            
            check[node] = 1
            # BackTrack
            path[node] = 0
            return False
                    
        
        visited = [0] * V
        path = [0] * V
        check = [0] * V
        res = []
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
                
        
        for i in range(V):
            if check[i] == 1:
                res.append(i)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends
