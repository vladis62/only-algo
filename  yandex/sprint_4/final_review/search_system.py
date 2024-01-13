# ID - 104816750
# -- ПРИНЦИП РАБОТЫ --
# Я реализовал поисковую систему, сначала построил индексы
# по полученным индексам ищем вхождение документа
# по полученным данным сделал сортировку и вывел первые 5 результатов
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# При индексации - O(N * K)
# При расчете релевантности - O(M * P * N)
# Получаем - O(N * K + M * P * N)
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Уникальных слов из всех документов (индексы) = O(K)
# Итоговый подсчет релевантных документов m = O(M)
# Получаем - O(K + M)
def build_index(documents):
    index = {}

    for i in range(1, len(documents) + 1):
        text = documents[i - 1].split()

        for word in text:
            if word in index:
                if i in index[word]:
                    index[word][i] += 1
                else:
                    index[word][i] = 1
            else:
                index[word] = {i: 1}

    return index


def process_query(index, queries):
    results = []

    for query in queries:
        words = set(query.split())
        query_result = {}

        for word in words:
            if word in index:
                for value in index[word]:
                    if value in query_result:
                        query_result[value] += index[word][value]
                    else:
                        query_result[value] = index[word][value]
        arr = sorted(query_result.items(), key=lambda x: (-x[1], x[0]))
        results.append([x[0] for x in arr[:5] if x[0] > 0])

    return results


def main():
    n = int(input())
    documents = [input() for _ in range(n)]

    m = int(input())
    queries = [input() for _ in range(m)]
    indexes = build_index(documents)
    [print(*m) for m in process_query(indexes, queries)]


if __name__ == '__main__':
    main()
