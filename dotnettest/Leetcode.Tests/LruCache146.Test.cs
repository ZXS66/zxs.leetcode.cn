namespace Leetcode.Tests;

public class LruCache146Test
{
    [Fact]
    public void LRUCache()
    {
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.Put(1, 1); // 缓存是 {1=1}
        lRUCache.Put(2, 2); // 缓存是 {1=1, 2=2}
        var result1 = lRUCache.Get(1);    // 返回 1
        Assert.Equal(1, result1);
        lRUCache.Put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
        var result2 = lRUCache.Get(2);    // 返回 -1 (未找到)
        Assert.Equal(-1, result2);
        lRUCache.Put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
        var result3 = lRUCache.Get(1);    // 返回 -1 (未找到)
        Assert.Equal(-1, result3);
        var result4 = lRUCache.Get(3);    // 返回 3
        Assert.Equal(3, result4);
        var result5 = lRUCache.Get(4);    // 返回 4
        Assert.Equal(4, result5);
        LRUCache lRUCache2 = new LRUCache(2);
        lRUCache2.Put(2, 1);
        lRUCache2.Put(1, 1);
        lRUCache2.Put(2, 3);
        lRUCache2.Put(4, 1);
        var result6 = lRUCache2.Get(1);
        Assert.Equal(-1, result6);
        var result7 = lRUCache2.Get(2);
        Assert.Equal(3, result7);
    }
}
