
# https://leetcode.cn/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150

"""
有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 
字母异位词
。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
 

提示:

1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s) != len(t): return False
        return all(s.count(c) == t.count(c) for c in set(s))
