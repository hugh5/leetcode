from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def post_order(node, level):
            if not node:
                return
            if len(result) == level:
                result.append([node.val])
            else:
                result[level].append(node.val)

            post_order(node.left, level + 1)
            post_order(node.right, level + 1)
        post_order(root, 0)
        return result



if __name__ == '__main__':
    s = Solution()
    print(s.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))