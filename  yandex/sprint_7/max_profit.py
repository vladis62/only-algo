def max_profit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit


def main():
    n = int(input())
    prices = list(map(int, input().split()))
    print(max_profit(prices))


if __name__ == '__main__':
    main()
