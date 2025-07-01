package zxs.leetcode.cn;

import java.util.HashMap;

public class LeetcodeTestCase {
    private HashMap<String, Object> _input;
    @SuppressWarnings("unchecked")
    public <T> T getInputByKey(String key) {
        return _input.containsKey(key) ? (T)_input.get(key) : null;
    }

    private Object _output;
    @SuppressWarnings("unchecked")
    public <T> T getOutput() {
        return (T) _output;
    }
    
    public LeetcodeTestCase(Object output, HashMap<String, Object> input) {
        this._output = output;
        this._input = input;
    }
}
