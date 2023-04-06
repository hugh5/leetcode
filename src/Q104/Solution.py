"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
leaf node.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.mdHelper(root, 0)
    def mdHelper(self, node: Optional[TreeNode], depth: int) -> int:
        if node is None:
            return depth

        return max(self.mdHelper(node.left, depth + 1), self.mdHelper(node.right, depth + 1))

if __name__ == '__main__':
    s = Solution()
    t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.maxDepth(t))