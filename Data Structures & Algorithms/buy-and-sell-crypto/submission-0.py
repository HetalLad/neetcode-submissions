class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p=prices[0]
        length=0
        max_p=0
        for p in range(1,len(prices)):
            if prices[p]<min_p:
                min_p=prices[p]
            elif prices[p] - min_p > max_p:
                max_p = prices[p] - min_p

        return max_p