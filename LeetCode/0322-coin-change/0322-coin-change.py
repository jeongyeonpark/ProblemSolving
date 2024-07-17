class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        #print(dp)
        for coin in coins:
            for x in range(coin, amount + 1):
                #print(f'coin:{coin},  x:{x},  dp[x]:{dp[x]},  dp[x-coin]+1:{dp[x - coin] + 1}')
                dp[x] = min(dp[x], dp[x - coin] + 1)
                #print(f'  {dp}')
        
        return dp[amount] if dp[amount] != float('inf') else -1