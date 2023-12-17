# ID - 100652172

# -- ПРИНЦИП РАБОТЫ --
# Я реализовал двусвязную очередь на массиве используя кольцевой буфер.
# Все добавляемые в начало очереди элементы добавляются конец стека со смещением влево.
# Все добавляемые в конец очереди элементы добавляются начало стека со смещением вправо.
# Все извлекаемые из начала очереди элементы извлекаются по индексу и индекс смещяется вправо.
# Все извлекаемые из конца очереди элементы извлекаются по индексу и индекс смещяется влево.
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# В целом описал вверху

# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# Добавление в начало и конец очереди стоит O(1), потому что добавление во входной стек стоит O(1).
# Извлечение из начала и конца очереди стоит O(1), так как храним значение индекса начала и конца.
#
# При n запросах к deque, сложность каждой операции будет всегда O(1) так как нет копирования массива
# и мы всегда манипулируем только индексом. В итоге все запросы к deque выполнятся за n.
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Очередь состоит из m элементов на протяжении всей работы программы
# Так же есть 4 переменных типа int


class Deque:
    def __init__(self, max_size):
        self.length = 0
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.deque = [None] * max_size

    def push_back(self, value):
        if self.max_size == self.length:
            raise IndexError
        self.deque[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.length += 1

    def push_front(self, value):
        if self.max_size == self.length:
            raise IndexError
        self.head = (self.head - 1 + self.max_size) % self.max_size
        self.deque[self.head] = value
        self.length += 1

    def pop_front(self):
        if self.length == 0:
            raise IndexError
        value = self.deque[self.head]
        self.head = (self.head + 1) % self.max_size
        self.length -= 1
        return value

    def pop_back(self):
        if self.length == 0:
            raise IndexError
        self.tail = (self.tail - 1 + self.max_size) % self.max_size
        value = self.deque[self.tail]
        self.length -= 1
        return value


def main():
    n = int(input())
    size = int(input())
    deque = Deque(size)
    for _ in range(n):
        cmd = input().split()
        try:
            if cmd[0] == 'push_back':
                deque.push_back(cmd[1])
            elif cmd[0] == 'push_front':
                deque.push_front(cmd[1])
            elif cmd[0] == 'pop_front':
                print(deque.pop_front())
            else:
                print(deque.pop_back())
        except IndexError:
            print('error')


if __name__ == '__main__':
    main()
