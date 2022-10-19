package Q1;

import java.util.HashMap;

public class Solution {

    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i = 0; i < nums.length; i++){
            int pair = (target - nums[i]);
            if(map.containsKey(pair)){
                return new int[]{map.get(pair), i};
            }

            map.put(nums[i], i);
        }
        return null;
    }

    public static void main(String[] args) {
        int[] ans = twoSum(new int[]{3,2,4}, 6);
        System.out.printf("[%d, %d]", ans[0], ans[1]);
    }
}
