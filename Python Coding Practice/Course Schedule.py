#User function Template for python3
from collections import deque
class Solution:
    
    def findOrder(self,N,P,prerequisites):
        
        adj =[[]for _ in range(N)]
        
        
        for u, v in prerequisites:
            adj[v].append(u)
            
        res = []
        Indegree = [0] * N
        
        Q = deque()
            
            
        for i in range(N):
            for node in adj[i]:
                Indegree[node] += 1
        
        
        for i in range(N):
            if Indegree[i] == 0:
                Q.append(i)
        
        while Q:
            node = Q.popleft()
            res.append(node)
            
            for i in adj[node]:
                Indegree[i] -= 1
                
                if Indegree[i] == 0:
                    Q.append(i)
        
        if len(res) == N:
            return res
        return []


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends
