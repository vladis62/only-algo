# ID - 104922647
# -- ПРИНЦИП РАБОТЫ --
# Я реализовал поисковую систему, сначала построил индексы
# по полученным индексам ищем вхождение документа
# по полученным данным сделал сортировку и вывел первые 5 результатов
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# При индексации - O(n * k)
# При расчете релевантности - O(m * p * n)
# Получаем - O(n * k + m * p * n)
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Уникальных слов из всех документов (индексы) = O(k)
# Итоговый подсчет релевантных документов m = O(m)
# Получаем - O(k + m)
def build_index(documents):
    index = {}

    for i in range(1, len(documents) + 1):
        text = documents[i - 1].split()

        for word in text:
            if word in index:
                index[word][i] = index[word].get(i, 0) + 1
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
                    query_result[value] = query_result.get(value, 0) + index[word][value]
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
