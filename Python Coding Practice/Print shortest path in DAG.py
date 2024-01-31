from typing import List, Tuple
from queue import PriorityQueue

class Solution:
    def dijkstra(self, V: int, adj: List[List[Tuple[int, int]]], S: int, T: int) -> List[int]:
        dist = [float("inf")] * (V + 1)
        parent = [i for i in range(V + 1)]

        pq = PriorityQueue()
        dist[S] = 0
        pq.put((0, S))

        while not pq.empty():
            P_dis, P_node = pq.get()

            for C_node, C_dis in adj[P_node]:
                if C_dis + P_dis < dist[C_node]:
                    dist[C_node] = C_dis + P_dis
                    parent[C_node] = P_node
                    pq.put((C_dis + P_dis, C_node))
        
        path = []
        node = V
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(S)
        return path[::-1]

if __name__ == "__main__":
    
    V = 5
    adj = [[(1, 1), (2, 3), (4, 4)], 
           [(0, 1), (2, 1), (3, 2)],
           [(0, 3), (1, 1)],
           [(1, 2)],
           [(0, 4)]]
    S = 0 
    T = 4 

    obj = Solution()
    shortest_path = obj.dijkstra(V, adj, S, T)
    print("Shortest path from vertex", S, "to vertex", T, ":", shortest_path)

