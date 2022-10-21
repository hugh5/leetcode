package Q219;

import java.util.HashMap;

public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>(nums.length);
        for (int i = 0; i < nums.length; i++) {
            Integer old = map.put(nums[i], i);
            if (old != null && i - old <= k) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution q219 = new Solution();
        int[] nums = new int[]{1,2,3,1,2,3};
        int k = 2;
        System.out.println(q219.containsNearbyDuplicate(nums,k));
    }
}
