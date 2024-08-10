class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
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