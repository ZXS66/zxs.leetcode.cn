# https://leetcode.cn/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        if ns < nt:
            return ""
        s_counter = Counter()
        t_counter = Counter(t)
        answer_left = -1  # -1 表示整个 s 都不满足要求
        answer_right = ns
        left = 0
        for right, c in enumerate(s):  # 移动右指针
            s_counter[c] += 1
            while s_counter >= t_counter:  # 满足条件：s 子串已包含 t，移动左指针
                if right - left < answer_right - answer_left:  # 找到更小子串
                    answer_left, answer_right = left, right
                s_counter[s[left]] -= 1
                left += 1
        return "" if answer_left == -1 else s[answer_left : answer_right + 1]
