from collections import Counter


def maxScoreWords(words, letters, score):
    # Calculate the score for each word
    def word_score(word):
        return sum(score[ord(char) - ord('a')] for char in word)

    # Convert letters list to a counter for easy frequency calculation
    letter_count = Counter(letters)

    # Convert words to list of (word, word_score)
    word_scores = [(word, word_score(word)) for word in words]

    # Memoization dictionary
    memo = {}

    def backtrack(index, remaining_letters):
        if index == len(words):
            return 0

        # Convert remaining_letters to a tuple to use it as a key for memoization
        key = (index, tuple(sorted(remaining_letters.items())))
        if key in memo:
            return memo[key]

        max_score = 0

        # Skip the current word
        max_score = backtrack(index + 1, remaining_letters)

        # Try to use the current word if possible
        word, word_score = word_scores[index]
        word_count = Counter(word)

        if all(remaining_letters[char] >= word_count[char] for char in word_count):
            # Create a new remaining_letters after using the current word
            new_remaining_letters = remaining_letters.copy()
            for char in word_count:
                new_remaining_letters[char] -= word_count[char]

            # Calculate score including this word
            max_score = max(max_score, word_score + backtrack(index + 1, new_remaining_letters))

        memo[key] = max_score
        return max_score

    return backtrack(0, letter_count)


# Example usage
words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "g", "o", "o"]
score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(maxScoreWords(words, letters, score))  # Output: 23
