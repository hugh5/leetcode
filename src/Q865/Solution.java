package Q865;

import java.util.HashMap;
import java.util.Objects;

class Solution {
    private static HashMap<Integer, Integer> depthMap;
    public static TreeNode subtreeWithAllDeepest(TreeNode root) {
        // <Node Value, Depth>
        depthMap = new HashMap<>();
        postOrderPutDepth(root, 0);
        return findSubTree(root);
    }

    public static void postOrderPutDepth(TreeNode root, int depth) {
        if (root.left != null) {
            postOrderPutDepth(root.left, depth + 1);
        }
        if (root.right != null) {
            postOrderPutDepth(root.right, depth + 1);
        }
        int leftDepth = root.left == null ? depth : depthMap.get(root.left.val);
        int rightDepth = root.right == null ? depth : depthMap.get(root.right.val);
        depthMap.put(root.val, Math.max(leftDepth, rightDepth));
    }

    public static TreeNode findSubTree(TreeNode root) {
        if (root.left == null && root.right == null) {
            return root;
        }
        if (root.left == null) {
            findSubTree(root.right);
            return findSubTree(root.right);
        }
        if (root.right == null) {
            return findSubTree(root.left);
        }
        int leftDepth = depthMap.get(root.left.val);
        int rightDepth = depthMap.get(root.right.val);
        if (leftDepth == rightDepth) {
            return root;
        }
        return leftDepth > rightDepth ? findSubTree(root.left) : findSubTree(root.right);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3, new TreeNode(5, new TreeNode(6), new TreeNode(2, new TreeNode(7), new TreeNode(4))), new TreeNode(1, new TreeNode(0), new TreeNode(8)));
//        root = new TreeNode(0, new TreeNode(1, null, new TreeNode(2)), new TreeNode(3));
        root = subtreeWithAllDeepest(root);
        System.out.println(root.val);
    }
}