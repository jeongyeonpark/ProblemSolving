class Solution:
    def canJump(self, nums: List[int]) -> bool:
        result = [0]+[inf]*(len(nums)-1)
        for i in range(len(nums)-1):
            if result[i] != inf:
                for j in range(1,nums[i]+1):
                    if i+j >= len(nums)-1:
                        return True
                    result[i+j] = min(result[i]+1, result[i+j])

        if result[-1] != inf:
            return True
        return False