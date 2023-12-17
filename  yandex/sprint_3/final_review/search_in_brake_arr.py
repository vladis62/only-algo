# ID - 103183092
# -- ПРИНЦИП РАБОТЫ --
# Я реализовал bin search в отсортированном массиве со сдвигом пользуясь
# базовыми принципами бинарного поиска
# основной принцип работы в том, чтобы отслеживать в какую границу мы попали
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# O(log(N)) - разделяй и властвуй.
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Дополнительных массивов не создается, только 3 переменных
# l и r - каждый раз меняется значение в ссылке, m каждый цикл новая создается

def broken_search(nums, target) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) >> 1
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if nums[l] < target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target < nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


def main():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    broken_search(arr, 5)
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    main()
