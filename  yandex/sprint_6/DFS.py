def dfs(graph, start_vertex):
    history = set()
    traversal = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in history:
            history.add(vertex)
            traversal.append(vertex)
            reversed_edges = reversed(graph[vertex])
            stack.extend(reversed_edges)
    return traversal


def edges_to_adjacency_list(edges):
    adjacency_list = {}
    edges.sort()
    for edge in edges:
        if edge[0] not in adjacency_list:
            adjacency_list[edge[0]] = [edge[1]]
        else:
            adjacency_list[edge[0]].append(edge[1])
    return adjacency_list


def main():
    n, m = map(int, input().split())

    edges = []

    for it in range(m):
        row, column = map(int, input().split())
        edges.append((row, column))
        edges.append((column, row))

    adjacency_list = edges_to_adjacency_list(edges)

    for row in range(1, n + 1):
        if adjacency_list.get(row) is None:
            adjacency_list[row] = []

    print(*dfs(adjacency_list, int(input())))


if __name__ == '__main__':
    main()
