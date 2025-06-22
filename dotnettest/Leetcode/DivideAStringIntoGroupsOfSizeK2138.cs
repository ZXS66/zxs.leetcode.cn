// https://leetcode.cn/problems/divide-a-string-into-groups-of-size-k/description/?envType=daily-question&envId=2025-06-22
public class Solution2138
{
    public string[] DivideString(string s, int k, char fill)
    {
        var res = new List<string>();
        int idx = 0;
        while (idx < s.Length)
        {
            if (idx + k <= s.Length)
            {
                res.Add(s.Substring(idx, k));
            }
            else
            {
                res.Add(s.Substring(idx).PadRight(k, fill));
            }
            idx += k;
        }
        return res.ToArray();
    }
}