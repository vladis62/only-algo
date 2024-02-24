# ID - 107924674

# -- ПРИНЦИП РАБОТЫ --
# Мы используем heapq для хранения самого тяжёлого ребра в остовном дереве.
# Функция add_vertex() проверяет и добавляет вершины в остов, используя min_heap для сортировки ребер по весу.
# Для поиска максимального остовного дерева мы начинаем обход графа с одной вершины и добавляем ребра в дерево,
# пока не покроем все вершины
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
#  O(E * log(V)), E - количество рёбер в графе, V - количество вершин.
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
#  O(n) - Хранение кучи.
#  O(E + V) - Список смежности, E - количество вершин, V - количество рёбер.

import heapq


def add_vertex_to_tree(vertex, edges_of_vertex, added_vertices, edge_heap):
    added_vertices[vertex] = True
    for edge, weight in edges_of_vertex:
        if not added_vertices[edge]:
            heapq.heappush(edge_heap, (-weight, edge))


def build_graph(num_vertices, num_edges):
    graph = [[] for _ in range(num_vertices + 1)]

    for _ in range(num_edges):
        from_vertex, to_vertex, weight = map(int, input().split())
        graph[from_vertex].append((to_vertex, weight))
        graph[to_vertex].append((from_vertex, weight))

    return graph


def calculate_maximum_spanning_tree(graph, num_vertices):
    added_vertices, edge_heap = [False] * (num_vertices + 1), []
    maximum_spanning_tree_weight = 0

    added_vertices[0] = True
    add_vertex_to_tree(1, graph[1], added_vertices, edge_heap)

    while any(added_vertices) and edge_heap:
        weight, vertex = heapq.heappop(edge_heap)
        if not added_vertices[vertex]:
            maximum_spanning_tree_weight += abs(weight)
            add_vertex_to_tree(vertex, graph[vertex], added_vertices, edge_heap)

    return 'Oops! I did it again' if not all(added_vertices) else maximum_spanning_tree_weight


def main():
    num_vertices, num_edges = map(int, input().split())
    graph = build_graph(num_vertices, num_edges)
    result = calculate_maximum_spanning_tree(graph, num_vertices)
    print(result)


if __name__ == '__main__':
    main()
