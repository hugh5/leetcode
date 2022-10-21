package Q217;

import java.util.HashMap;

public class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap();
        for (int n : nums) {
            if (map.put(n, n) != null) return true;
        }
        return false;
    }
}
