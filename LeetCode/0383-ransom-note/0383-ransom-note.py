class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """for rn in ransomNote:
            if ransomNote.count(rn) > magazine.count(rn):
                return False
                break
        return True"""

        mag_list = [x for x in magazine]
        for rn in ransomNote:
            if rn in mag_list:
                mag_list.remove(rn)
            else:
                return False
        return True