from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        valid = True
        def in_order(node):
            nonlocal prev
            nonlocal valid
            if not node:
                return
            in_order(node.left)
            if prev is not None and prev > node.val:
                valid = False
            prev = node.val
            in_order(node.right)

        in_order(root)
        return valid


if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST(TreeNode(0, None, TreeNode(-1))))
    # print(s.isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))
    # print(s.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))))