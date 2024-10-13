class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        muaximum_profit = 0
        min_stock = prices[0]

        for price in prices:
            if price < min_stock:
                min_stock = price

            if price-min_stock > muaximum_profit:
                muaximum_profit = price-min_stock

        return muaximum_profit