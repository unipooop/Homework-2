def find_profitable_path(graph, start, visited, path, balance, max_balance, max_path):
    visited.add(start)
    path.append(start)

    if len(path) > 1:
        prev_token = path[-2]
        profit = balance * graph[(prev_token, start)][1] / graph[(prev_token, start)][0]
        balance -= profit

    if balance > max_balance:
        max_balance = balance
        max_path = path.copy()

    for neighbor in graph:
        if neighbor[0] == start and neighbor[1] not in visited:
            max_balance, max_path = find_profitable_path(graph, neighbor[1], visited, path, balance, max_balance, max_path)

    visited.remove(start)
    path.pop()

    return max_balance, max_path

liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

graph = liquidity.copy()
for edge in liquidity:
    reverse_edge = (edge[1], edge[0])
    graph[reverse_edge] = (liquidity[edge][1], liquidity[edge][0])

start_token = "tokenB"
visited = set()
path = []
balance = 1.0  # Starting balance
max_balance, max_path = find_profitable_path(graph, start_token, visited, path, balance, 0, [])

print("Path:", "->".join(max_path), ", Balance:", max_balance)

