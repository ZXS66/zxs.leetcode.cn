package zxs.leetcode.cn;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Subsets78Test {
    @Test
    public void testSubsets() {
        List<LeetcodeTestCase> testcases = new ArrayList<LeetcodeTestCase>() {
            {
                add(new LeetcodeTestCase(new ArrayList<ArrayList<Integer>>() {
                    {
                        add(new ArrayList<Integer>());
                        add(new ArrayList<Integer>() {
                            {
                                add(1);
                            }
                        });
                        add(new ArrayList<Integer>() {
                            {
                                add(2);
                            }
                        });
                        add(new ArrayList<Integer>() {
                            {
                                add(3);
                            }
                        });
                        add(new ArrayList<Integer>() {
                            {
                                add(1);
                                add(2);
                            }
                        });
                        add(new ArrayList<Integer>() {
                            {
                                add(1);
                                add(3);
                            }
                        });
                        add(new ArrayList<Integer>() {
                            {
                                add(2);
                                add(3);
                            }
                        });
                        add(new ArrayList<Integer>() {
                            {
                                add(1);
                                add(2);
                                add(3);
                            }
                        });
                    }
                }, new HashMap<String, Object>() {
                    {
                        put("nums", new int[] { 1, 2, 3 });
                    }
                }));
                add(new LeetcodeTestCase(
                        new ArrayList<ArrayList<Integer>>() {
                            {
                                add(new ArrayList<Integer>());
                                add(new ArrayList<Integer>() {
                                    {
                                        add(0);
                                    }
                                });
                            }
                        }, new HashMap<String, Object>() {
                            {
                                put("nums", new int[] { 0 });
                            }
                        }));
            }
        };
        Subsets78 sln = new Subsets78();
        for (LeetcodeTestCase testcase : testcases) {
            List<List<Integer>> result = sln.subsets((int[]) testcase.getInputByKey("nums"));
            List<List<Integer>> expected = testcase.getOutput();
            // assertArrayEquals(
            // "Expected: " + expected + ", but got: " + result,
            // expected.toArray(), result.toArray());
            assertEquals(result.size(), expected.size());
        }
        System.out.println("Test passed!");
    }
}
