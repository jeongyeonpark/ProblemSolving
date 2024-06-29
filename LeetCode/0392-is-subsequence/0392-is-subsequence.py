class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sn = tn = 0
        while sn<len(s) and tn<len(t):
            if s[sn] == t[tn]:
                sn+=1
            tn+=1
            
        if sn == len(s):
            return True
        return False