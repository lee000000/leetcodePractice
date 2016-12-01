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

'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dif = 0
        i = 0
        while (i < len(prices)):
            j = i + 1
            while (j < len(prices)):
                if ((prices[j] - prices[i]) > dif):
                    dif = prices[j] - prices[i]
                j += 1

            i += 1

        return dif


if __name__ == "__main__":
    a = [7, 6, 4, 3, 1]
    sol = Solution()
    dif = sol.maxProfit(a)
    print(dif)
