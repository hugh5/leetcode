package Q8;

class Solution {
    public int myAtoi(String s) {
        s = s.trim();
        if (s.isEmpty()) {
            return 0;
        }
        boolean negative = false;
        if (s.charAt(0) == '-') {
            negative = true;
            s = s.substring(1);
        } else if (s.charAt(0) == '+') {
            s = s.substring(1);
        }
        int i;
        for (i = 0; i < s.length(); i++) {
            if (!Character.isDigit(s.charAt(i))) {
                break;
            }
        }
        s = (String) s.subSequence(0, i);
        int num = 0;
        for (i = 0; i < s.length(); i++) {
            if (negative) {
                num -= Integer.parseInt(String.valueOf(s.charAt(s.length() - 1 - i))) * Math.pow(10, i);
            } else {
                num += Integer.parseInt(String.valueOf(s.charAt(s.length() - 1 - i))) * Math.pow(10, i);
            }
        }
        return num;
    }
}