#User function Template for python3

from typing import List
from collections import deque

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        Indegree = [0]*V
        adjRev = [[]for _ in range(V)]
        Q = deque()
        res = []
        
        for i in range(V):
            for node in adj[i]:
                adjRev[node].append(i)
                Indegree[i] += 1
        
        for i in range(V):
            if Indegree[i] == 0:
                Q.append(i)
        
        while Q:
            node = Q.pop()
            res.append(node)
            
            for k in adjRev[node]:
                Indegree[k] -= 1
                
                if Indegree[k] == 0:
                    Q.append(k)
                    
        sorted_res = sorted(res)
        return sorted_res

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
