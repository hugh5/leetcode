package Q110;

class Solution {
    private boolean balanced;
    public boolean isBalanced(TreeNode root) {
        balanced = true;
        if (root == null) return true;
        postOrderDepth(root, 0);
        return balanced;
    }

    public int postOrderDepth(TreeNode root, int depth) {
        int leftDepth = root.left == null ? depth : postOrderDepth(root.left, depth + 1);
        int rightDepth = root.right == null ? depth : postOrderDepth(root.right, depth + 1);
        if (Math.abs(leftDepth - rightDepth) >= 2) balanced = false;
        return Math.max(leftDepth, rightDepth);
    }

    public static void main(String[] args) {
        Solution q110 = new Solution();
        TreeNode root;
        root = new TreeNode(10, new TreeNode(19, new TreeNode(7, new TreeNode(4), new TreeNode(5)), new TreeNode(8)), null);
        System.out.println(q110.isBalanced(root));
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