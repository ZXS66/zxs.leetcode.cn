# https://leetcode.cn/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for item in strs:
            while item[0 : len(prefix)] != prefix:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
