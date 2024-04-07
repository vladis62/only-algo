def get_card_count(n, k, cards) -> int:
    l = k - 1
    r = n - 1
    max_sum = prefix_sum = sum(cards[:k])

    while l >= 0:
        print(prefix_sum, cards[l], cards[r])
        prefix_sum = prefix_sum - cards[l] + cards[r]
        max_sum = max(prefix_sum, max_sum)
        l -= 1
        r -= 1

    return max_sum


n = int(input())
k = int(input())
cards = list(map(int, input().split()))

print(get_card_count(n, k, cards))
