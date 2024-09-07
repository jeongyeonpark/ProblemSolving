class Solution:
    def reverseBits(self, n: int) -> int:   
        result = 0
        x = 31
        while n!=0:
            if n >= 2**x:
                n-=2**x
                result+= 2**(31-x)
            x-=1
        return result