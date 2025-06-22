//https://leetcode.cn/problems/find-all-anagrams-in-a-string/?envType=study-plan-v2&envId=top-100-liked

public class FindAllAnagramsInAString438
{
    public IList<int> FindAnagrams(string s, string p)
    {
        IList<int> res = new List<int>();
        int ns = s.Length, np = p.Length;

        Func<string, IDictionary<char, int>> getCounter = (string str) =>
        {
            IDictionary<char, int> counter = new Dictionary<char, int>();
            if (!string.IsNullOrEmpty(str))
            {
                foreach (var ch in str)
                {
                    if (!counter.ContainsKey(ch))
                    {
                        counter.Add(ch, 1);
                    }
                    else
                    {
                        counter[ch]++;
                    }
                }
            }
            return counter;
        };
        Func<IDictionary<char, int>, IDictionary<char, int>, bool> isSameCounter = (IDictionary<char, int> counter1, IDictionary<char, int> counter2) =>
        {
            if (counter1.Count != counter2.Count)
                return false;
            foreach (var kv in counter1)
            {
                if (!(counter2.ContainsKey(kv.Key) && kv.Value == counter2[kv.Key]))
                    return false;
            }
            return true;
        };

        if (ns >= np)
        {
            var counterP = getCounter(p);
            int cursor = 0;
            int lastCursor = -1;
            while (cursor <= ns - np)
            {
                if (cursor > 0 && cursor == lastCursor + 1 && s[lastCursor] == s[cursor+np-1])
                {
                    // quick check if the popup item s[lastCursor] and the new pushed item s[cursor+np] are the same
                    res.Add(cursor);
                    lastCursor = cursor;
                    cursor++;
                    continue;
                }

                var counterS = getCounter(s.Substring(cursor, np));
                if (isSameCounter(counterS, counterP))
                {
                    res.Add(cursor);
                    lastCursor = cursor;
                }
                cursor++;
            }
        }
        return res;
    }
}