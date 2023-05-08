from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for val in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, val)
            elif self.heap[0] < val:
                heapq.heappushpop(self.heap, val)
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]



if __name__ == '__main__':
    k = KthLargest(3, [4, 5, 8, 2])
    print(k.add(3))
    print(k.add(5))
    print(k.add(10))
    print(k.add(9))
    print(k.add(4))