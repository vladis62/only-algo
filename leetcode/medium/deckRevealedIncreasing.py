from collections import deque


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck = sorted(deck, reverse=True)
        reveal_order = deque()

        for card in deck:
            if reveal_order:
                reveal_order.appendleft(reveal_order.pop())

            reveal_order.appendleft(card)

        return list(reveal_order)


deck = [17, 13, 11, 2, 3, 5, 7]
print(Solution().deckRevealedIncreasing(deck))
