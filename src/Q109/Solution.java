package Q109;

public class Solution {
    private ListNode current;
    public TreeNode sortedListToBST(ListNode head) {
        current = head;
        int length = length(head);
        return createSubTree(length);
    }

    // O(n) to get length of list
    public int length(ListNode head) {
        int l = 0;
        while (head != null) {
            head = head.next;
            l++;
        }
        return l;
    }

    public TreeNode createSubTree(int n) {
        if (n == 0) return null;
        TreeNode left = createSubTree(n / 2);
        TreeNode root = new TreeNode(current.val);
        root.left = left;
        current = current.next;
        root.right = createSubTree(n - 1 - n/2);
        return root;
    }

    public void inOrder(TreeNode root) {
        if (root == null) return;
        inOrder(root.left);
        System.out.println(root.val);
        inOrder(root.right);
    }

    public static void main(String[] args) {
        Solution q109 = new Solution();
        ListNode head;
        head = new ListNode(0, new ListNode(3, new ListNode(4, new ListNode(8, new ListNode(16, new ListNode(20))))));
//        head = new ListNode(1, new ListNode(2, new ListNode(3)));

        TreeNode ans = q109.sortedListToBST(head);
//        q109.inOrder(ans);
    }
}