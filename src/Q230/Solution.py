from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = 0

        def in_order(node):
            nonlocal count
            nonlocal result
            if result != 0:
                return
            if node.left is not None:
                in_order(node.left)
            count += 1
            if count == k:
                result = node.val
                return
            if node.right is not None:
                in_order(node.right)

        in_order(root)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest(TreeNode(3, TreeNode(1, right=TreeNode(2)), TreeNode(4)), 2))
