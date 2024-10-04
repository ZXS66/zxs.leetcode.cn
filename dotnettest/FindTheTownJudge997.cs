// https://leetcode.cn/problems/find-the-town-judge/description/?envType=daily-question&envId=2024-09-22

public class Solution997
{
    // trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
    public int FindJudge(int n, int[][] trust)
    {
        // you trust others
        IDictionary<int, int> trustA = new Dictionary<int, int>();
        // others that trust you
        IDictionary<int, int> trustB = new Dictionary<int, int>();
        foreach (var t in trust)
        {
            trustA[t[0]] = trustA.ContainsKey(t[0]) ? trustA[t[0]] + 1 : 1;
            trustB[t[1]] = trustB.ContainsKey(t[1]) ? trustB[t[1]] + 1 : 1;
        }
        for (int i = 1; i <= n; i++)
        {
            if (!trustA.ContainsKey(i) && trustB.ContainsKey(i) && trustB[i] == n - 1)
            {
                return i;
            }
        }
        if (n == 1 && !trust.Any()) return 1;   // edge case: n = 1, trust = []
        return -1;
    }
}

