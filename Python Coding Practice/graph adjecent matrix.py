n,m = map(int,input().split())
adj_list = []
for i in range(n):
    row = [0 for j in range(n)]
    adj_list.append(row)

for k in range(m):
    adj_list[u][v] = 1
    adj_list[v][u] = 1

print(adj_list)
