class Solution:
    def trailingZeroes(self, n: int) -> int:
        total_n = 0
        while n:
            x = n//5
            total_n+=x
            n = x
        return total_n