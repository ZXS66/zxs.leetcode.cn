package zxs.leetcode.cn;

import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;

import org.junit.Test;

public class FindTheOriginalTypedStringI3330Test {
    @Test
    public void testPossibleStringCount() {
        List<LeetcodeTestCase> testcases = new ArrayList<LeetcodeTestCase>() {
            {
                add(new LeetcodeTestCase(1, new HashMap<String, Object>() {
                    {
                        put("word", "a");
                    }
                }));
                add(new LeetcodeTestCase(5, new HashMap<String, Object>() {
                    {
                        put("word", "abbcccc");
                    }
                }));
                add(new LeetcodeTestCase(1, new HashMap<String, Object>() {
                    {
                        put("word", "abcd");
                    }
                }));
                add(new LeetcodeTestCase(4, new HashMap<String, Object>() {
                    {
                        put("word", "aaaa");
                    }
                }));
            }
        };
        FindTheOriginalTypedStringI3330 sln = new FindTheOriginalTypedStringI3330();
        for (LeetcodeTestCase testcase : testcases) {
            int result = sln.possibleStringCount((String) testcase.getInputByKey("word"));
            int expected = testcase.getOutput();
            assertTrue(
                    "Expected: " + expected + ", but got: " + result,
                    result == expected);
        }
    }
}
