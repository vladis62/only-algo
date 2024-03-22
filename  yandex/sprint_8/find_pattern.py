def find_pattern(measurements, pattern):
    indexes = []
    for i in range(len(pattern) - 1, len(measurements)):
        offset: int = i - (len(pattern) - 1)
        measurements_slice = measurements[offset : i + 1]
        diff = set((x - y for x, y in zip(measurements_slice, pattern)))
        if len(diff) == 1:
            indexes.append(offset + 1)
    return indexes


def main() -> None:
    _ = int(input())
    measurements = list(map(int, input().split()))
    _ = int(input())
    pattern = list(map(int, input().split()))
    print(*find_pattern(measurements, pattern))


if __name__ == "__main__":
    main()
