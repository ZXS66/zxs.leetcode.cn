package zxs.leetcode.cn;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import org.junit.Test;

public class SlidingWindowMaximum239Test {

    @Test
    public void testMaxSlidingWindow() {
        List<LeetcodeTestCase> testcases = new ArrayList<LeetcodeTestCase>() {
            {
                add(new LeetcodeTestCase(new int[] { 3,3,5,5,6,7 }, new HashMap<String, Object>() {
                    {
                        put("nums", new int[] {1,3,-1,-3,5,3,6,7 });
                        put("k", 3);
                    }
                }));
                add(new LeetcodeTestCase(new int[] { 5, 6, 7 }, new HashMap<String, Object>() {
                    {
                        put("nums", new int[] { 5, 5, 6, 7 });
                        put("k", 2);
                    }
                }));
            }
        };

        SlidingWindowMaximum239 solution = new SlidingWindowMaximum239();
        for (LeetcodeTestCase testcase : testcases) {
            int[] expected = testcase.getOutput();
            int[] output = solution.maxSlidingWindow(
                    testcase.getInputByKey("nums"),
                    testcase.getInputByKey("k"));
            assertEquals(expected.length, output.length);
            assertArrayEquals(expected, output);
        }
    }
}
