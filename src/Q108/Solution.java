package Q108;

class Solution {
    private int[] nums;
    public TreeNode sortedArrayToBST(int[] nums) {
        this.nums = nums;
        return createBST(null,0, nums.length - 1);
    }

    public TreeNode createBST(TreeNode node, int lower, int upper) {
        int diff = upper - lower;
        int mid = (upper + lower) / 2;
        if (node == null) {
            node = new TreeNode(nums[mid]);
        }
        if (diff == 0) {
            return new TreeNode(nums[mid]);
        }
        if (diff == 1) {
            return new TreeNode(nums[lower], null, new TreeNode(nums[upper]));
        }
        node.left = createBST(node.left, lower, mid - 1);
        node.right = createBST(node.right, mid + 1, upper);
        return node;
    }

    public void inOrder(TreeNode root) {
        if (root == null) return;
        inOrder(root.left);
        System.out.println(root.val);
        inOrder(root.right);
    }

    public static void main(String[] args) {
        Solution q108 = new Solution();
        TreeNode ans;
        ans = q108.sortedArrayToBST(new int[]{-10,-3,0,5,9});
        q108.inOrder(ans);

        ans = q108.sortedArrayToBST(new int[]{0,1,2,3,4,5});
        q108.inOrder(ans);
    }
}
