class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, i = len(nums), 0
        while val in nums:# and k<len(nums):
            while nums[i] == val:
                nums[i] = '_'
                if k==1:
                    return 0
                nums[i],nums[k-1] = nums[k-1], nums[i]
                k-=1
            i+=1
        return k