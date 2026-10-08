class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        delta = 0

        for sell in range(len(prices)):
            if(prices[sell] < prices[buy]):
                buy = sell
            else:
                curr = prices[sell]-prices[buy]
                if(curr > delta):
                    delta = curr
        if(delta<0):
            return 0
        return delta