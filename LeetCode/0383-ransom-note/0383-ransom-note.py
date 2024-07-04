class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for rn in ransomNote:
            if ransomNote.count(rn) > magazine.count(rn):
                return False
        return True