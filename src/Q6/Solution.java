package Q6;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static String convert(String s, int numRows) {
        if (numRows < 2) return s;
        int currentRow = 0;
        int zig = 1;
        List<List<Character>> list = new ArrayList<>(numRows);
        for (int i = 0; i < s.length(); i++) {
            List<Character> level;
            if (i % (2*numRows - 2) == 0) {
                zig = 1;
                currentRow = 0;
            } else if (i % (2*numRows - 2) == numRows-1) {
                zig = -1;
                currentRow = numRows - 1;
            }
            if (i < numRows) {
                level = new ArrayList<>();
                level.add(s.charAt(i));
                list.add(level);
            } else {
                level = list.get(currentRow);
                level.add(s.charAt(i));
            }
            currentRow += zig;
        }
        StringBuilder result = new StringBuilder(s.length());
        for (List<Character> level : list) {
            for (Character c : level) {
                result.append(c);
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        System.out.println(convert("PAYPALISHIRING", 2));
    }
}
