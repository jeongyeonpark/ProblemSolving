class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            idx = haystack.find(needle)
            return idx
        else:
            return -1