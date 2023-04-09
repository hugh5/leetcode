import math
from typing import Optional

"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""


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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast is not None:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next

        if slow == head:
            return None
        if slow.next is None:
            head.next = None
            return head

        slow.val = slow.next.val
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    s = Solution()
    print(s.deleteMiddle(ListNode(1)))
    print(s.deleteMiddle(ListNode(1, ListNode(2))))
    print(s.deleteMiddle(ListNode(1, ListNode(2, ListNode(3)))))
    print(s.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
    print(s.deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))