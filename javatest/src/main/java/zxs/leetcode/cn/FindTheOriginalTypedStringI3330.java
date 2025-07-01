package zxs.leetcode.cn;

public class FindTheOriginalTypedStringI3330 {
    public int possibleStringCount(String word) {
        int count = 1;
        int n = word.length();
        int i = 0;
        while (i < n - 1) {
            char currentChar = word.charAt(i);
            int j = i + 1;
            while (j < n && word.charAt(j) == currentChar) {
                j++;
            }
            if (j - i > 1) {
                count += j - i - 1; // Count the number of ways to form the original string
            }
            i = j;
        }
        return count;
    }
}
