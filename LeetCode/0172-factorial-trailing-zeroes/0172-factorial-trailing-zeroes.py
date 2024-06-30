class Solution:
    def trailingZeroes(self, n: int) -> int:
        n2 = 0
        n5 = 0
        while n > 1:
            x = n
            if x%2 == 0:
                while x%2 == 0:
                    n2+=1
                    x = x/2
            if x%5 == 0:
                while x%5 == 0:
                    n5+=1
                    x = x/5
            n-=1

        if n2 < n5 :
            return n2
        return n5