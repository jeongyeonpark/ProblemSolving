class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        longest_len = 0
        for word in s.split():
            word_len = len(word)
            if longest_len < word_len:
                longest_len = word_len
        return word_len