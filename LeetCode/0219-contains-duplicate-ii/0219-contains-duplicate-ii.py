class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     li = {}
    #     for idx,val in enumerate(nums):
    #         if not val in li:
    #             li[val] = idx
    #         elif abs(li[val]-idx) <= k:
    #             return True
    #         else:
    #             li[val] = idx
    #     return False

        li = set()
        i = 0
        for val in nums:
            if val in li:
                return True
            li.add(val)
            if len(li) > k:
                li.remove(nums[i-k])
            i+=1
        return False