class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_ = set(numbers)
        for i in range(len(numbers)):
            if target-numbers[i] in numbers_:
                for j in range(i+1, len(numbers)):
                    if numbers[j] == target-numbers[i]:
                        return [i+1, j+1]
        