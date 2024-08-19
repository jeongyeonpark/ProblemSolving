class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            for j in range(1, nums[i]+1):
                if i + j < n:
                    dp[i+j] = min(dp[i+j], dp[i] + 1)

        return dp[n-1]

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         def run(idx, depth):
#             poss_idx = [idx+d for d in range(1,nums[idx]+1)]
#             print(poss_idx)
#             for idx_ in poss_idx:
#                 if idx_ >= len(nums)-1:
#                     print(f'>> {idx}, {nums[idx_]}')
#                     return depth
#                 return run(idx_, depth+1)

#         result = run(0, 0)
#         print(f'result: {result}')
#         return result
        