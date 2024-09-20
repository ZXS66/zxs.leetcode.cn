// https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/description/?envType=daily-question&envId=2024-09-19

public class Solution2414
{
    public int LongestContinuousSubstring(string s)
    {
        if (String.IsNullOrEmpty(s)) return 0;
        if (s.Length == 1) return 1;
        int max = 0;
        int cur = 0;
        char lastChar = s[0];
        foreach (var c in s)
        {
            if (cur == 0)
            {
                max = cur = 1;
                continue;
            }
            else
            {
                if (c - lastChar == 1)
                {
                    cur++;
                    max = Math.Max(max, cur);
                }
                else
                {
                    cur = 1;
                }
                lastChar = c;
            }
        }
        return max;
    }
}