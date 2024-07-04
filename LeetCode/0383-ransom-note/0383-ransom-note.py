class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_list = [x for x in magazine]
        for rn in ransomNote:
            if rn in mag_list:
                mag_list.remove(rn)
            else:
                return False
        return True