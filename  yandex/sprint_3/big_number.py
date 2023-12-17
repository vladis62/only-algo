def build_big_number(arr):
    insertion_sort_by_comparator(arr, is_first_big_number)
    return "".join(arr)


def is_first_big_number(card_1, card_2):
    return int(card_1 + card_2) > int(card_2 + card_1)


def insertion_sort_by_comparator(array, more):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and more(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert


def main():
    _ = int(input())
    arr = list(map(str, input().split()))
    print(build_big_number(arr))


if __name__ == '__main__':
    main()
