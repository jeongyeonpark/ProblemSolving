class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import numpy as np
        result = [1]*len(nums)
        
        # for i,n in enumerate(nums):
        #     for j in range(len(nums)):
        #         if i != j:
        #             result[i] = result[i]*nums[j]

        # return result

        if 0 in nums:
            nums2 = nums.copy()
            nums2.remove(0)
            total = np.prod(nums2)
            for i,n in enumerate(nums):
                if n != 0:
                    result[i] = 0
                else:
                    result[i] = total
        else:
            total = np.prod(nums)
            for i,n in enumerate(nums):
                result[i] = int(total/n)
        return result