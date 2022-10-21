package Q655;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    private static List<List<String>> list;
    private static int height;
    public static List<List<String>> printTree(TreeNode root) {
        height = getDepth(root, 0);
        list = new ArrayList<>(height + 1);
        putVal(root, 0, 0);
        for (List<String> l : list) {
            while (l.size() < Math.pow(2, height + 1) - 1) {
                l.add("");
            }
        }
        return list;
    }

    public static int getDepth(TreeNode node, int depth) {
        if (node == null) return depth-1;
        return Math.max(getDepth(node.left, depth+1), getDepth(node.right, depth+1));
    }

    public static void putVal(TreeNode node, int depth, int leftness) {
        if (depth > height) return;
        List<String> level;
        if (leftness == 0) {
            level = new ArrayList<>((int) Math.pow(2, height + 1) - 1);
            for (int i = 0; i < Math.pow(2, height - depth) - 1; i++) {
                level.add("");
            }
            list.add(level);
        } else {
            level = list.get(depth);
            for (int i = 0; i < Math.pow(2, height - depth + 1) - 1; i++) {
                level.add("");
            }
        }
        String val = node == null ? "" : String.valueOf(node.val);
        level.add(val);
        putVal(node == null ? null : node.left, depth+1, leftness);
        putVal(node == null ? null : node.right, depth+1, leftness+1);
    }

    public static void main(String[] args) {
        TreeNode root;
        root = new TreeNode(0, new TreeNode(1, null, new TreeNode(2, new TreeNode(3), null)), new TreeNode(1, null, new TreeNode(2, null, new TreeNode(3))));
//        root = new TreeNode(1, new TreeNode(2), new TreeNode(1));
        printTree(root);
        for (List<String> l : list) {
            for (String s : l) {
                System.out.print(s);
            }
            System.out.println();
        }
    }
}
