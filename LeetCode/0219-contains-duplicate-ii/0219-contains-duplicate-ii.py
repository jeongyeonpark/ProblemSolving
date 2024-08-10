class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        li = {}
        for idx,val in enumerate(nums):
            if val in li and idx-li[val]<=k:
                return True
            else:
                li[val] = idx
        return False