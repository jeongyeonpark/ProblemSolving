class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            digits[-1] = 10
            i = -1
            while digits[i] > 9:
                if len(digits) <= abs(i):
                    digits[i] = 0
                    return [1] + digits
                digits[i] = 0
                digits[i-1] = digits[i-1]+1
                i-=1
            return digits

        else:
            return digits[:-1] + [digits[-1]+1]
