package Q7;

import java.util.LinkedList;

public class Solution {
    public static int reverse(int x) {
        LinkedList<Integer> digits = new LinkedList<>();
        int numDigits = 0;
        while (x != 0) {
            digits.add(x % 10);
            x /= 10;
            numDigits++;
        }
        int rev = 0;
        for (Integer digit : digits) {
            rev += Math.pow(10,numDigits-- - 1) * digit;
        }
        if (rev == Integer.MAX_VALUE || rev == Integer.MIN_VALUE) rev = 0;
        return rev;
    }

    public static void main(String[] args) {
//        reverse(213);
        System.out.println(reverse(-2147483648));
    }
}