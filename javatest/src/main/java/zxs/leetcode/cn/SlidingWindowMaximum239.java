package zxs.leetcode.cn;

import java.util.ArrayList;
import java.util.List;

public class SlidingWindowMaximum239 {

    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k <= 0) {
            return new int[0];
        }

        List<Integer> result = new ArrayList<>();
        int n = nums.length;
        int maxIndex = 0, maxValue = nums[0];
        for (int i = 0; i < n; i++) {
            if (i < k - 1) {
                // Update maxValue for the first k-1 elements
                if (nums[i] > maxValue) {
                    maxValue = nums[i];
                    maxIndex = i;
                }
            } else {
                // Remove the element that is sliding out of the window
                if (i - k == maxIndex) {
                    // maxValue was the first element that slidding out of the window
                    // Find the new maxValue in the current window
                    if (nums[i] > maxValue) {
                        maxValue = nums[i];
                        maxIndex = i;
                    } else if (nums[i - k + 1] == maxValue) {
                        maxIndex = i - k + 1;
                    } else {
                        maxIndex = i - k + 1;
                        maxValue = nums[maxIndex];
                        for (int j = i - k + 2; j <= i; j++) {
                            if (nums[j] > maxValue) {
                                maxValue = nums[j];
                                maxIndex = j;
                            }
                        }
                    }
                } else if (nums[i] > maxValue) {
                    // Update maxValue if the new element is greater
                    maxValue = nums[i];
                    maxIndex = i;
                }
                result.add(maxValue);
            }
        }
        // Convert List<Integer> to int[]
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
