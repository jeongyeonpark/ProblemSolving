class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_i = -1
        end_i = -1

        for idx, n in enumerate(nums):
            if n > target:
                break

            if n == target:
                if start_i == -1:
                    start_i = idx
                    end_i = idx
                else:
                    end_i = idx

        if start_i == -1 or end_i == -1:
            return [-1, -1]
        else:
            return [start_i, end_i]