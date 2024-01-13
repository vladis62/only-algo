# ID 104826138
# -- ПРИНЦИП РАБОТЫ --
# Реализовал простую хеш-таблицу с тремя методами.
# В качестве вспомогательной структуры данных использовал массив массивов
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Все операции работают за O(1) в лучшем случае
# Модуль - размер вспомогательной структуры, подобран исходя из количества входящих операций
# В связи с этим коллизии встречаются редко и O(N) в операциях мало вероятен
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Размер вспомогательной структуры - O(N)
class Map:
    def __init__(self, size):
        self.size = size
        self.arr = [[] for _ in range(size)]

    def put(self, key, value):
        index = self.hash(key)
        for pair in self.arr[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.arr[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        for pair in self.arr[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash(key)
        for i, pair in enumerate(self.arr[index]):
            if pair[0] == key:
                value = pair[1]
                del self.arr[index][i]
                return value
        return None

    def hash(self, key):
        return key % self.size


def main():
    n = int(input())
    map = Map(n)
    for i in range(0, n):
        line = input().split()
        if line[0] == 'get':
            key = int(line[1])
            print(map.get(key))
        elif line[0] == 'put':
            key, value = int(line[1]), int(line[2])
            map.put(key, value)
        else:
            key = int(line[1])
            print(map.delete(key))


if __name__ == '__main__':
    main()
