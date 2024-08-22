class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_n = 0
        word = set()
        l = 0
        for i in range(len(s)):
            if not s[i] in word:
                word.add(s[i])
            else:
                if max_n < len(word):
                    max_n = len(word)
                while s[i] in word:
                    word.remove(s[l])
                    l+=1
                word.add(s[i])

        return max(max_n, len(word))