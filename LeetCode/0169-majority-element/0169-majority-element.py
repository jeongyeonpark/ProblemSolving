class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        min_n = len(nums)/2
        li = {}
        for n in nums:
            if n in li:
                li[n]+=1
            else:
                li[n]=1
        for i in li:
            if li[i]>min_n:
                return i