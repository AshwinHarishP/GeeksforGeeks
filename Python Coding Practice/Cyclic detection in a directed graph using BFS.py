#User function Template for python3

from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        Q = deque()
        Indegree = [0]*V
        res = []
        
        for i in range(V):
            for node in adj[i]:
                Indegree[node] += 1
        
        for i in range(V):
            if Indegree[i] == 0:
                Q.append(i)
                
        while Q:
            node = Q.popleft()
            res.append(node)
            
            for i in adj[node]:
                Indegree[i] -= 1
                if Indegree[i] == 0:
                    Q.append(i)
        return len(res) != len(Indegree)
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends
