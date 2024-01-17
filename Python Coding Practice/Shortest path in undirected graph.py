#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        def toposort(node):
            visited[node] = 1
            
            for v, _ in adj[node]:
                if not visited[v]:
                    toposort(v)
            st.append(node)
            
        adj = [[]for _ in range(n)]
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))
            
        visited = [0]*n
        
        # Find the topo sort
        st = []
        for i in range(n):
            if not visited[i]:
                toposort(i)
                
        # Step 2. Do the distance thing
        distance = [float('inf')]* n
        distance[0] = 0
        
        while st:
            node = st.pop()
            
            for v, w in adj[node]:
                if distance[node] + w < distance[v]:
                    distance[v] = distance[node] + w
                    
        for i in range(n):
            if distance[i] == float('inf'):
                distance[i] = -1
        distance[0] = 0
        return distance
            
            
#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends
