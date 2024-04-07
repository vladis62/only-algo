# https://leetcode.com/problems/word-search/description/

# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

class Solution(object):
    def exist(self, board, word):
        def find_word(word, row, col):
            if not word:
                return True

            if row < 0 or row == len(board) or col < 0 or col == len(board[0]) or board[row][col] != word[0]:
                return False

            temp, board[row][col] = board[row][col], '-1'

            result = find_word(word[1:], row + 1, col) or find_word(word[1:], row - 1, col) or find_word(word[1:], row, col + 1) or find_word(word[1:], row, col - 1)

            board[row][col] = temp

            return result

        for i in range(len(board)):
            for j in range(len(board[i])):
                if find_word(word, i, j):
                    return True

        return False



print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB"))
print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE"))
print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
