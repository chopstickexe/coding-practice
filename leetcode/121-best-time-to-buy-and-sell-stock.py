# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = 10000
        for p in prices:
            if profit < (p - min_price):
                profit = p - min_price
            if p < min_price:
                min_price = p
        return profit
