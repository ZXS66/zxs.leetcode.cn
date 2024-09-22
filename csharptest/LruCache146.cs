// https://leetcode.cn/problems/lru-cache/description/?envType=study-plan-v2&envId=top-interview-150


public class LRUCache
{
    private Dictionary<int, int> _cache = new Dictionary<int, int>();
    private List<int> _usedKeys = new List<int>();
    private int _capacity;

    public LRUCache(int capacity)
    {
        _capacity = capacity;
    }

    public int Get(int key)
    {
        if (_cache.ContainsKey(key))
        {
            _usedKeys.Remove(key);
            _usedKeys.Add(key);
            return _cache[key];
        }
        return -1;
    }

    public void Put(int key, int value)
    {
        if (_cache.ContainsKey(key))
        {
            _usedKeys.Remove(key);
            _usedKeys.Add(key);
            _cache[key] = value;
        }
        else
        {
            if (_cache.Count == _capacity)
            {
                int keyToRemove = _usedKeys[0];
                _usedKeys.RemoveAt(0);
                _cache.Remove(keyToRemove);
            }
            _usedKeys.Add(key);
            _cache.Add(key, value);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */