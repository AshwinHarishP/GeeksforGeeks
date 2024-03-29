#User function Template for python3

from typing import List
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        bfs = []
        visited = [False] * V
        Q = deque()
        
        Q.append(0)
        visited[0] = True
        
        while Q:
            node = Q.popleft()
            bfs.append(node)
            
            for i in adj[node]:
                if not visited[i]:
                    Q.append(i)
                    visited[i] = True
        return bfs


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends
