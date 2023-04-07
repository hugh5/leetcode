"""
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0, 1, 1]
        for i in range(3, n + 1):
            nums.append(nums[i - 3] + nums[i - 2] + nums[i - 1])
        return nums[n]


if __name__ == '__main__':
    s = Solution()
    print(s.tribonacci(25))
