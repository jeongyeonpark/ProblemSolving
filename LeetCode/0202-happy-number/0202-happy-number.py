class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while not n in nums:
            nums.add(n)
            new_n = 0
            for v in str(n):
                new_n+= int(v)*int(v)
            n = new_n

        if n == 1:
            return True
        return False