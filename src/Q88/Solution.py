from typing import List

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To
accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and
the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        iter1, iter2 = iter(nums1[:m]), iter(nums2)
        num1 = next(iter1, None)
        num2 = next(iter2, None)
        i = 0
        while num1 is not None and num2 is not None:
            if num1 < num2:
                nums1[i] = num1
                num1 = next(iter1, None)
            else:
                nums1[i] = num2
                num2 = next(iter2, None)
            i += 1

        while num1 is not None:
            nums1[i] = num1
            num1 = next(iter1, None)
            i += 1

        while num2 is not None:
            nums1[i] = num2
            num2 = next(iter2, None)
            i += 1



if __name__ == '__main__':
    s = Solution()
    l1, l2 = list((1, 2, 3, 0, 0, 0)), list((2, 5, 6))
    s.merge(l1, 3, l2, 3)
    print(l1)
    assert l1 == list((1, 2, 2, 3, 5, 6))
