from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return sum(piles[0::2]) != sum(piles[1::2])
