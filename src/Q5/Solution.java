package Q5;

public class Solution {
    public static String longestPalindrome(String s) {
        for (int j = s.length(); j >= 0; j--) {
            for (int i = 0; i <= s.length() - j; i++) {
                if (isPalindrome(s.substring(i, j + i))) {
                    return s.substring(i, j + i);
                }
            }
        }
        return "";
    }

    public static boolean isPalindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
//        isPalindrome("Hello");
        System.out.println(longestPalindrome("abcdefghijk"));
        System.out.println(longestPalindrome("cbbd"));
    }
}
