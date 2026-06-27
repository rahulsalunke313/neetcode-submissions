class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        buy = prices[0]
        for i in prices[1:]:
            buy = min(i,buy)
            maxx = max(i-buy, maxx)
        return maxx

