import heapq
from typing import List

"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance i.e., √((x1 - x2)^2 + (y1 - y2)^2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            heapq.heappush(minheap, ((x ** 2) + (y ** 2), [x, y]))

        return [value[1] for value in heapq.nsmallest(k, minheap)]


if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))
