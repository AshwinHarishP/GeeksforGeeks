#User function Template for python3
from collections import deque
class Solution:
    def isPossible(self,N,P,prerequisites):
        
        adj =[[]for _ in range(N)]
        
        
        for u, v in prerequisites:
            adj[u].append(v)
            
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
        
        return len(res) == len(Indegree)
                
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,P,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
