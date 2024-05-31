from collections import deque


class Solution(object):
    def countStudents(self, students, sandwiches):
        student_queue = deque(students)
        sandwich_stack = list(sandwiches)

        attempts_since_last_sandwich = 0

        while student_queue and attempts_since_last_sandwich < len(student_queue):
            if student_queue[0] == sandwich_stack[0]:
                student_queue.popleft()
                sandwich_stack.pop(0)
                attempts_since_last_sandwich = 0
            else:
                student_queue.rotate(-1)
                attempts_since_last_sandwich += 1

        return len(student_queue)


print(Solution().countStudents(students=[0, 0, 0, 1, 1, 1, 1, 0, 0, 0], sandwiches=[1, 0, 1, 0, 0, 1, 1, 0, 0, 0]))
