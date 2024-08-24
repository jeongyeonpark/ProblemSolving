class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return  max(nums)
        
        n1 = nums[0]
        n2 = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            if n2 < n1+nums[i]:
                curr_n = n1+nums[i]
                n1 = n2
                n2 = curr_n
            else:
                n1 =  n2
        return n2