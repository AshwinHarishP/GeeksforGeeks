from collections import deque

class Solution:
    def isBipartite(self, V, adj):
        def check(start):
            Q = deque()
            Q.append(start)
            color[start] = 0

            while Q:
                node = Q.popleft()
                for i in adj[node]:
                    if color[i] == -1:
                        # If the adjacent node is not colored, then color them using the opposite color
                        color[i] = not color[node]
                        Q.append(i)

                    # If the adjacent node has colored
                    # i -> parent, node -> current node
                    elif color[i] == color[node]:
                        return False
            return True

        color = [-1] * V

        for i in range(V):
            if color[i] == -1:
                if not check(i):
                    return False

        return True
		
	
		            
		            

#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
