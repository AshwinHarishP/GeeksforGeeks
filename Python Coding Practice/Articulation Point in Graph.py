class Solution:
    def __init__(self):
        self.timer = 1

    def dfs(self, node, parent, vis, tin, low, mark, adj):
        vis[node] = 1
        tin[node] = low[node] = self.timer
        self.timer += 1
        child = 0
        for it in adj[node]:
            if it == parent:
                continue
            if not vis[it]:
                self.dfs(it, node, vis, tin, low, mark, adj)
                low[node] = min(low[node], low[it])
                if low[it] >= tin[node] and parent != -1:
                    mark[node] = 1
                child += 1
            else:
                low[node] = min(low[node], tin[it])
        if child > 1 and parent == -1:
            mark[node] = 1

    def articulationPoints(self, n, adj):
        vis = [0] * n
        tin = [-1] * n
        low = [-1] * n
        mark = [0] * n
        for i in range(n):
            if not vis[i]:
                self.dfs(i, -1, vis, tin, low, mark, adj)
        ans = [i for i in range(n) if mark[i] == 1]
        if not ans:
            return [-1]
        return ans


if __name__ == "__main__":
    n = 5
    edges = [
        [0, 1], [1, 4],
        [2, 4], [2, 3], [3, 4]
    ]
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    obj = Solution()
    nodes = obj.articulationPoints(n, adj)
    print(*nodes)
