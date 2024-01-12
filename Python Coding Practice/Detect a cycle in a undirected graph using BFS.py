from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		def is_detect(src):
		    Q = []
		    vis[src] = 1
		    Q.append([src, -1])
		    
		    while Q:
		        node = Q[0][0]
		        parent = Q[0][1]
		        Q.pop(0)
		        
		        
		        for i in adj[node]:
		            if not vis[i]:
		                vis[i] = 1
		                Q.append([i, node])
		            
		            elif i != parent:
		                return True
		    return False
		            
		
		
		
		vis = [0] * V
		for i in range(V):
		    if not vis[i]:
		        if is_detect(i):
		            return True
		return False

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
