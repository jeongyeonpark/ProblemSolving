class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        end_x = len(grid[0])
        end_y = len(grid)

        dp = [[0]*end_x for _ in range(end_y)]
        dp[0][0] = grid[0][0]

        v = dp[0][0]
        for i in range(1,end_x):
            dp[0][i] = v + grid[0][i]
            v = dp[0][i]

        v = dp[0][0]
        for j in range(1,end_y):
            dp[j][0] = v + grid[j][0]
            v = dp[j][0]

        for x in range(1,end_x):
            for y in range(1,end_y):
                dp[y][x] = min(dp[y-1][x], dp[y][x-1]) + grid[y][x]

        return dp[-1][-1]

