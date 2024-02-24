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
        r, c = map(int, input().split())
        edges.append((r, c))

    adjacency_list = edges_to_adjacency_list(edges)

    for row in range(1, n + 1):
        if row in adjacency_list:
            print(len(adjacency_list[row]), *adjacency_list[row])
        else:
            print(0)


if __name__ == '__main__':
    main()
