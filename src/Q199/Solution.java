package Q199;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.TreeSet;

public class Solution {
    private ArrayList<Integer> list;
    public List<Integer> rightSideView(TreeNode root) {
        list = new ArrayList<>();
        rootRightLeft(root, 0);
        return list;
    }

    public void rootRightLeft(TreeNode node, int depth) {
        if (node == null) return;
        if (list.size() == depth) {
            list.add(node.val);
        }
        rootRightLeft(node.right, depth+1);
        rootRightLeft(node.left, depth+1);
    }

    public class TreeNode {
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

}
