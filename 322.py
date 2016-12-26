'''
322. Coin Change

You are given coins of different denominations and a total

amount of money amount. Write a function to compute the fewest

number of coins that you need to make up that amount. If that

amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''
import sys
class Solution(object):
    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        need = [0] + [sys.maxsize] * (amount)
        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    need[i] = min(need[i], need[i - coin] + 1)

        return -1 if need[-1] > amount else need[-1]


    # naive DP
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        print(('amount,', amount))
        if amount == 0:
            return 0
        n = amount + 1
        for coin in coins:
            curCount = 0
            if coin <= amount:
                next = self.coinChange(coins, amount - coin)
                print('next,', next)
                print('coin,', coin)
                if next >= 0:
                    curCount = 1 + next
            if curCount > 0:
                n = min(n, curCount)
        if n == amount + 1:
            return -1
        else:
            return n


def test():
    coins = [2147483647]
    amount = 2
    sol = Solution()
    print(sol.coinChange2(coins, amount))


if __name__ == "__main__":
    test()
