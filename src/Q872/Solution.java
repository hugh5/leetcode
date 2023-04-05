package Q872;

import java.util.LinkedList;
import java.util.List;

class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaves = new LinkedList<>();
        leaves = inOrder1(root1, leaves);
        return inOrder2(root2, leaves) && leaves.size() == 0;
    }

    public List<Integer> inOrder1(TreeNode treeNode, List<Integer> leaves) {
        if (treeNode == null) {
            return leaves;
        }
        if (treeNode.left == null && treeNode.right == null) {
            leaves.add(treeNode.val);
            return leaves;
        }
        if (treeNode.left != null) {
            leaves = inOrder1(treeNode.left, leaves);
        }
        if (treeNode.right != null) {
            leaves = inOrder1(treeNode.right, leaves);
        }
        return leaves;
    }

    public boolean inOrder2(TreeNode treeNode, List<Integer> leaves) {
        if (treeNode == null) {
            return true;
        }
        if (leaves.size() == 0) return false;
        if (treeNode.left == null && treeNode.right == null) {
            return treeNode.val == leaves.remove(0);
        }
        boolean inorderLeft = true;
        boolean inorderRight = true;
        if (treeNode.left != null) {
            inorderLeft = inOrder2(treeNode.left, leaves);
        }
        if (treeNode.right != null) {
            inorderRight = inOrder2(treeNode.right, leaves);
        }
        return inorderLeft && inorderRight;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}