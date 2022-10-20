package Q189;

import java.util.Arrays;

public class Solution {
    // O(1) extra space
    public static void rotate(int[] nums, int k) {
        int swaps = 0;
        for (int c = 0; swaps < nums.length; c++) {
            int old = nums[c];
            int temp;
            int i = c;
            do {
                System.out.printf("i:%d, next:%d\n", i, (i + k) % nums.length);
                temp = nums[(i + k) % nums.length];
                nums[(i + k) % nums.length] = old;
                old = temp;
                i = (i + k) % nums.length;
                swaps++;
            } while (i != c);
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[]{0,1,2,3,4, 5};
        rotate(nums, 7);
        System.out.println(Arrays.toString(nums));
    }
}
