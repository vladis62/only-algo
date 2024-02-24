# ID - 108035680

# -- ПРИНЦИП РАБОТЫ --
# Для определения оптимальности карты железных дорог можно построить граф,
# поменяв направление ребер для одного типа дороги, и применить обход DFS на каждой вершине.
# Если в процессе обхода обнаруживается цикл, значит путь неоптимальный.
# Использую алгоритм обнаружения цикла в ориентированном графе с помощью цветовой классификации вершин.
# Обходя граф, помечаем вершины тремя цветами (белый, серый, черный).
# Если встречаем серую вершину, это означает наличие цикла.
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
#  O(n^2) - из каждого города даны дороги во все следующие города.
#  Количество дорог n-1 + n-2 + ... + 2 + 1, то есть n^2/2 или O(n^2).
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
#   O(n), n - количество вершин в графе.

WHITE = 'white'
GREY = 'grey'
BLACK = 'black'


def is_cycle(adjacency):
    colors = [WHITE] * len(adjacency)

    def dfs_is_cycle(start_vertex):
        stack = [start_vertex]

        while stack:
            v = stack.pop()
            if colors[v] == WHITE:
                stack.append(v)
                colors[v] = GREY

                for w in adjacency[v]:
                    if colors[w] == WHITE:
                        stack.append(w)
                    elif colors[w] == GREY:
                        return True
            elif colors[v] == GREY:
                colors[v] = BLACK

        return False

    return any(dfs_is_cycle(i) for i in range(len(adjacency)))


def main():
    n = int(input())
    adjacency = {v: [] for v in range(0, n)}

    for i in range(n - 1):
        for j, road in enumerate(input()):
            if road == 'B':
                adjacency[i].append(i + j + 1)
            else:
                adjacency[i + j + 1].append(i)

    print('NO' if is_cycle(adjacency) else 'YES')


if __name__ == '__main__':
    main()
