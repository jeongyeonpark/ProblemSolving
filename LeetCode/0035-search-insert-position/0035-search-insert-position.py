class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i<len(nums) and target > nums[i]:
            i+=1
        return i