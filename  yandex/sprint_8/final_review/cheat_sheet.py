# ID - 110306389
# -- ПРИНЦИП РАБОТЫ --
# Билдим префиксное дерево по строкам. Проходим по дереву и в dp пишем  True если достигли листового узла, иначе FALSE
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
#  O(k) + O(n**2), k - сумма всех слов, n - кол-во символов в строке
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
#  O(k), k - дерево, O(n) - массив  dp

class Node:
    def __init__(self, value, next=None):
        if next is None:
            next = {}
        self.value = value
        self.next = next
        self.is_terminal = False


def build_tree(strings):
    root = Node('')
    for word in strings:
        node = root
        # тут мы закинули слово в узлы
        for index, char in enumerate(word):
            node.next[char] = node.next.get(char, Node(char))
            node = node.next[char]
        # Тут понимаем, что это конечная буква при обходе во внутреннем цикле при составлении динамики
        # Может что угодно сюда поставить, главное не False
        node.is_terminal = True
    return root


def is_split_strings(string, strings):
    root = build_tree(strings)
    dp = [True] + [False] * len(string)
    for i in range(len(string)):
        node = root
        # - останавливаемся только на тех индексах, которые терминальные - исключение первый индекс
        if not dp[i]:
            continue
        for j in range(i, len(string) + 1):
            if node.is_terminal:
                dp[j] = True
            # - Если переменная j достигла длины строки, то цикл прерывается
            if j == len(string):
                break
            # - наличие следующего узла в дереве для текущей буквы строки
            next_node = node.next.get(string[j])
            if not next_node:
                break
            node = next_node
    return dp[-1]


def main():
    string = input()
    strings = [input() for _ in range(int(input()))]
    print('YES' if is_split_strings(string, strings) else 'NO')


if __name__ == '__main__':
    main()
