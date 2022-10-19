package Q28;

import java.util.HashMap;

/**
 * Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
 * or -1 if needle is not part of haystack.
 */
public class Solution {
    // Boyer-Moore
    public static int strStr(String haystack, String needle) {
        HashMap<Character, Integer> lastOccurrence = preProcess(needle);
        int n = haystack.length();
        int m = needle.length();

        int s = 0;
        while(s <= (n - m)) {
            int j = m-1;
            while(j >= 0 && needle.charAt(j) == haystack.charAt(s+j))
                j--;
            if (j < 0)
            {
                return s;
            }
            else {
                Integer last = lastOccurrence.get(haystack.charAt(s + j));
                last = last == null ? -1 : last;
                s += Math.max(1, j - last);
            }
        }
        return -1;
    }

    public static HashMap<Character, Integer> preProcess(String pattern) {
        HashMap<Character, Integer> lastOccurrence = new HashMap<>();
        for (int i = pattern.length() - 1; i >= 0; i--) {
            lastOccurrence.putIfAbsent(pattern.charAt(i), i);
        }
        return lastOccurrence;
    }

    public static void main(String[] args) {
        int index;
        String haystack;
        String needle;
        haystack = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut " +
                "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " +
                "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit " +
                "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt " +
                "in culpa qui officia deserunt mollit anim id est laborum.";
        needle = "laborum";

        index = strStr(haystack, needle);
        System.out.println(haystack.substring(index, index + needle.length()));
    }
}
