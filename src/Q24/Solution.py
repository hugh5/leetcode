"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the
values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = ""
        result += f"{self.val} -> "
        if self.next is not None:
            result += self.next.__str__()
        else:
            result = result.removesuffix(" -> ")
        return result

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newHead = None
        prev = None
        first = head
        second = head.next
        while True:
            first.next = second.next
            second.next = first
            if newHead is None:
                newHead = second
                prev = first
            else:
                prev.next = second
                prev = first
            if first.next is not None and first.next.next is not None:
                second = first.next.next
                first = first.next
            else:
                break
        return newHead

if __name__ == '__main__':
    s = Solution()
    l = ListNode(1)
    print(s.swapPairs(None))
    print(s.swapPairs(ListNode(1)))
    print(s.swapPairs(ListNode(1, ListNode(2))))
    print(s.swapPairs(ListNode(1, ListNode(2, ListNode(3)))))
    print(s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
    print(s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
    print(s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))))
    print(s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))))




