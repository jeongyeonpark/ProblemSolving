class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_elements = ['_']
        i = 0

        while i < len(nums):
            j = i+1
            e = nums[i]

            if not e in unique_elements:
                unique_elements.append(e)
            elif j < len(nums):
                nums[i] = '_'
                while nums[j] in unique_elements:
                    nums[j] = '_'
                    if j+1 >= len(nums):
                        break
                    j+=1
                if nums[j] == '_':
                    break
                unique_elements.append(nums[j])
                nums[j], nums[i] = nums[i], nums[j]
            i+=1
        if len(nums) == 1:
            return 1
        k = len(unique_elements)-1
        return k