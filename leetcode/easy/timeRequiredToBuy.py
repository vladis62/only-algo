from collections import deque


class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        tickets_queue = deque(tickets)
        result = 0

        while True:
            result += 1
            cnt = tickets_queue[0]
            cnt -= 1
            if k == 0 and cnt == 0:
                return result
            k = (k - 1) % len(tickets_queue)
            tickets_queue.popleft()
            if cnt > 0:
                tickets_queue.append(cnt)



# print(Solution().timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0))
print(Solution().timeRequiredToBuy(tickets=[2, 3, 2], k=2))
