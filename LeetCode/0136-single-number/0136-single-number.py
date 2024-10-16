class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_list = set()
        for num in nums:
            if num in num_list:
                num_list.remove(num)
            else:
                num_list.add(num)

        return list(num_list)[0]