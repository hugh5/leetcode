import heapq
from collections import Counter
from typing import List

"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time.
For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter 
in the array), that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        queue = []
        pq = list(map(lambda x: -x, freq.values()))
        heapq.heapify(pq)

        time = 0
        while any(queue) or len(pq) != 0:
            if queue and queue[0][0] < time:
                heapq.heappush(pq, queue.pop(0)[1])
            if len(pq) > 0:
                p = heapq.heappop(pq)
                if p < -1:
                    queue.append((time + n, p+1))
            time += 1
        return time


if __name__ == '__main__':
    s = Solution()
    print(s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
    print(s.leastInterval(["A","A","A","B","B","B"], 2))
    print(s.leastInterval(["A","A","A","B","B","B"], 0))
