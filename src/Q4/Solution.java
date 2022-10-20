package Q4;

import java.util.*;

public class Solution {
    public static double findMedianSortedArrays (int[] nums1, int[] nums2) {
        int length = nums1.length + nums2.length - 1;
        float mid = length / 2f;
        int[] median = new int[2];
        int[] merge = new int[(int) Math.ceil(mid) + 1];

        int a = 0, b = 0;
        for (int i = 0; i <= Math.ceil(mid); i++) {
            if (a >= nums1.length) {
                merge[i] = nums2[b++];
            } else if (b >= nums2.length) {
                merge[i] = nums1[a++];
            } else if (nums1[a] < nums2[b]) {
                merge[i] = nums1[a++];
            } else {
                merge[i] = nums2[b++];
            }
            if (i == Math.floor(mid)) {
                median[0] = merge[i];
            }
            if (i == Math.ceil(mid)) {
                median[1] = merge[i];
            }
        }
        return (median[0] + median[1]) / 2.0;
    }

    public static void main(String[] args) {
        System.out.println(findMedianSortedArrays(new int[]{1, 8, 12, 22, 27}, new int[]{2, 3, 5, 11, 17, 26}));
    }
}
