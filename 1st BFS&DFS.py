from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

def bfs(start):
    visited = set()
    queue = deque([start])
    print("BFS:", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

def dfs(start):
    visited = set()
    print("DFS:", end=" ")
    def dfs_util(node):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for n in graph[node]:
                dfs_util(n)
    dfs_util(start)

bfs(1)
print()
dfs(1)
