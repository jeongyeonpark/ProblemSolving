class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}
        x = set()
        for i in range(len(s)):
            if not s[i] in chars:
                if t[i] in x:
                    return False
                chars[s[i]] = t[i]
                x.add(t[i])
            else:
                if chars[s[i]] != t[i]:
                    return False
        return True