# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         result = [True]+[False]*(len(nums)-1)
#         for i in range(len(nums)-1):
#             if result[i] != False:
#                 for j in range(1,nums[i]+1):
#                     if i+j >= len(nums)-1:
#                         return True
#                     result[i+j] = True

#         return True if result[-1] != False else False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        leftTrue = len(nums)-1 # 4
        for i in range(len(nums)-2, -1, -1): # [3, 2, 1, 0]
            maxPosition = i + nums[i] # [4, 3, 4, 2]
            if maxPosition >= leftTrue:
                leftTrue = i

        return True if leftTrue == 0 else False