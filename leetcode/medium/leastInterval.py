from collections import Counter


def leastInterval(tasks, n):
    task_counts = Counter(tasks)

    max_freq = max(task_counts.values())

    max_freq_tasks = sum(1 for count in task_counts.values() if count == max_freq)

    return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_tasks)


tasks = ["A", "C", "A", "B", "D", "B"]
cooling_time = 2
print(leastInterval(tasks, cooling_time))  # Output should be 8
