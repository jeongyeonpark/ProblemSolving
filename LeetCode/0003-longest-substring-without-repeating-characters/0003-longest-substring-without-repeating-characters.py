class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_n = 0
        word = []
        for i in range(len(s)):
            if not s[i] in word:
                word.append(s[i])
            else:
                if max_n < len(word):
                    max_n = len(word)
                while s[i] in word:
                    word.pop(0)
                word.append(s[i])

        return max(max_n, len(word))