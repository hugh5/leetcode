from typing import Optional, List

"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value
sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves = []
        leaves = self.inOrder1(root1, leaves)
        return self.inOrder2(root2, leaves) and len(leaves) == 0

    def inOrder1(self, treeNode: Optional[TreeNode], leaves: List[int]) -> List[int]:
        if treeNode is None:
            return leaves
        if treeNode.left is None and treeNode.right is None:
            leaves.append(treeNode.val)
            return leaves
        if treeNode.left is not None:
            leaves = self.inOrder1(treeNode.left, leaves)
        if treeNode.right is not None:
            leaves = self.inOrder1(treeNode.right, leaves);
        return leaves

    def inOrder2(self, treeNode: Optional[TreeNode], leaves: List[int]) -> bool:
        if treeNode is None:
            return True
        if len(leaves) == 0:
            return False
        if treeNode.left is None and treeNode.right is None:
            return treeNode.val == leaves.pop(0)
        inorderLeft = True
        inorderRight = True
        if treeNode.left is not None:
            inorderLeft = self.inOrder2(treeNode.left, leaves)
        if treeNode.right is not None:
            inorderRight = self.inOrder2(treeNode.right, leaves)
        return inorderLeft and inorderRight
