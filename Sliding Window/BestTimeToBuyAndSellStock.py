class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #not optimized
       # maxProfit = 0
       # for i in range(len(prices)-1):
       #     buy = prices[i]
       #     sell = prices[i+1]
       #     for j in range(i+1, (len(prices))):
       #         sell = prices[j]
       #         if (buy < sell):
       #             if ((sell-buy) > maxProfit):
       #                 maxProfit = sell-buy
       # return maxProfit

        buy = 0
        sell = 1
        maxProfit = 0
        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy]
            if (prices[buy]< prices[sell]):
                maxProfit = max(currentProfit, maxProfit)
            else:
                buy = sell
            sell += 1 
        return maxProfit
