def calculate_total_area(heights, target_height):
    total_area = 0
    for i in range(1, len(heights)):
        if heights[i] < target_height:
            total_area += target_height - heights[i]
        else:
            total_area += heights[i] - target_height
    return total_area


def third_task(heights):
    left = min(heights)
    right = max(heights)

    while left <= right:
        mid = (left + right) // 2
        area = calculate_total_area(heights, mid)

        if area == 0:
            return mid
        elif area < 0:
            right = mid - 1
        else:
            left = mid + 1

    return left


def main():
    _ = input()
    heights = list(map(int, input().split()))
    print(third_task(heights))


if __name__ == '__main__':
    main()
