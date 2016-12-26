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

# This functioin count how many total ways to make the amount
# using coin set with infinite usage of each coin
# [1, 2], 3 --> 2
    def coinChange3(self, coins, amount):
        return self.helpCoinChange4(coins, len(coins), amount)


    def helpCoinChange3(self, coins, m, n):

        if n == 0: # to make 0, there is 1 solution
            return 1
        if n < 0: # could not find a combination
            return 0

        if m <= 0 and n >= 1: # n is not completed but coin set is empty
            return 0

        return self.helpCoinChange3(coins, m - 1, n) + self.helpCoinChange3(coins, m, n - coins[m - 1])

    def helpCoinChange4(self, coins, m, n):
        # We need n + 1 rows as the table is bottom up (tabulation) to find
        # possible ways to make each amount n
        # layer by layer fill the table from lower number to higher number
        table = [[0 for _ in range(m)] for _ in range(n + 1)]

        # first row of the table is 1
        for i in range(m):
            table[0][i] = 1

        # Fill rest of the table entries:
        for i in range(1, n + 1):
            for j in range(m):
                coin = coins[j]
                x = table[i - coin][j] if i - coin >= 0 else 0
                y = table[i][j - 1] if j >= 1 else 0
                table[i][j] = x + y

        return table[n][m - 1]


def test():
    coins = [2, 3, 5]
    amount = 11
    sol = Solution()
    print(sol.coinChange3(coins, amount))


if __name__ == "__main__":
    test()
