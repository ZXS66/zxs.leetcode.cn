package zxs.leetcode.cn;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import org.junit.Test;

import junit.framework.TestCase;

public class HelloTest extends TestCase {

//    public HelloTest(String testName) {
//        super(testName);
//    }

    @Test
    public void testSampleArray() {
        Hello hello = new Hello();
        int[] expected = { 1, 2, 3, 4, 5 };
        assertArrayEquals(expected, hello.sampleArray());
    }

    @Test
    public void testSampleString() {
        Hello hello = new Hello();
        String expected = "Hello, World!";
        assertEquals(expected, hello.sampleString());
    }
}
