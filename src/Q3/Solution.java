package Q3;

import java.util.HashMap;
import java.util.HashSet;

class Solution {
    public static int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> characters = new HashMap<>();
        int start = 0;
        int max = 0;
        for (int i = 0; i < s.length(); i++) {
            Integer old = characters.put(s.charAt(i), i);
            if (old != null) {
                start = Math.max(start, old + 1);
            }
            max = Math.max(max, i - start + 1);
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("abba"));
    }
}