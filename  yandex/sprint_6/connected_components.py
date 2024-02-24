def build_graph(n, m):
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = [int(i) - 1 for i in input().split()]
        graph[u].append(v)
        graph[v].append(u)
    return graph


def find_components(graph, n):
    visited = [False] * n
    result = 0
    components = []

    for i in range(n):
        if visited[i]:
            continue

        result += 1
        visited[i] = True
        queue = [i]
        component = []
        while queue:
            v = queue.pop()
            component.append(v + 1)
            for to in graph[v]:
                if not visited[to]:
                    visited[to] = True
                    queue.append(to)
        components.append(component)

    return result, components


def main():
    n, m = map(int, input().split())
    graph = build_graph(n, m)
    result, components = find_components(graph, n)

    print(result)
    for i in range(result):
        print(*sorted(components[i]))


if __name__ == "__main__":
    main()
