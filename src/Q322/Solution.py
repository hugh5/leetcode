from typing import List

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a 
total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
"""


class Solution:
    """
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

    Input: coins = [2], amount = 3
    Output: -1

    Input: coins = [1], amount = 0
    Output: 0
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        minNumber = [amount + 1 for _ in range(amount + 1)]
        minNumber[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    minNumber[a] = min(minNumber[a], 1 + minNumber[a - c])

        return minNumber[amount] if minNumber[amount] < amount + 1 else -1


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
    print(s.coinChange([2], 3))
    print(s.coinChange([1], 0))
