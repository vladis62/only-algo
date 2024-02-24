import collections


def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(str(vertex))

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return result


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

    result = bfs(adjacency_list, int(input()))
    print(" ".join(result))


if __name__ == '__main__':
    main()
