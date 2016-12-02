'''
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one

share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.


Dynamic Programming:
f(0) = 0 max = 0 min = 0 None or Null or n = 0

f(1) = 0 max = 0 min = prices[0] 1 element  or n = 1
f(2) = (dif = prices[1] - prices[0])  max = dif and min = min(prices[0], prices[1]) n = 2
f(3) = max (dif = prices[3] - min, max), max = f(3), min = min(min, prices[3]) n = 3

f(n) = max(prices[i] - min, f(n - 1)), min = min(prices[i], min)
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # TLE
        # dif = 0
        # i = 0
        # while (i < len(prices)):
        #     j = i + 1
        #     while (j < len(prices)):
        #         if ((prices[j] - prices[i]) > dif):
        #             dif = prices[j] - prices[i]
        #         j += 1
        #
        #     i += 1
        if not len(prices):
            return 0

        maxVal = [0] * (len(prices))
        minVal = prices[0]
        for i in range(len(prices)):
            maxVal[i] = max(prices[i] - minVal, maxVal[i - 1])
            minVal = min(prices[i], minVal)
            print(maxVal[i], minVal)
            i += 1
        print(maxVal)
        return maxVal[i - 1]


if __name__ == "__main__":
    a = [7, 1, 3, 5, 6, 4]
    sol = Solution()
    dif = sol.maxProfit(a)
    print(dif)
