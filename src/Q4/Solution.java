package Q4;

import java.util.*;

public class Solution {
    public static double findMedianSortedArrays (int[] nums1, int[] nums2) {
        float mid = (nums1.length + nums2.length - 1) / 2f;
        int[] median = new int[2];
        int current;

        int a = 0, b = 0;
        for (int i = 0; i <= Math.ceil(mid); i++) {
            if (a >= nums1.length) {
                current = nums2[b++];
            } else if (b >= nums2.length) {
                current = nums1[a++];
            } else if (nums1[a] < nums2[b]) {
                current = nums1[a++];
            } else {
                current = nums2[b++];
            }
            if (i == Math.floor(mid)) {
                median[0] = current;
            }
            if (i == Math.ceil(mid)) {
                median[1] = current;
            }
        }
        return (median[0] + median[1]) / 2.0;
    }

    public static void main(String[] args) {
        System.out.println(findMedianSortedArrays(new int[]{1, 8, 12, 22, 27}, new int[]{2, 3, 5, 11, 17, 26}));
    }
}
