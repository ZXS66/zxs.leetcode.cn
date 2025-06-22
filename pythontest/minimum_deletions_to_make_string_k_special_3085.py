# https://leetcode.cn/problems/minimum-deletions-to-make-string-k-special/?envType=daily-question&envId=2025-06-21

from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        ct = Counter(word)
        if len(ct) <= 1:
            return 0
        deletions = len(word)
        values = list(ct.values())
        for v1 in values:
            temp = 0
            for v2 in values:
                if v1 > v2:
                    temp += v2	# delete all occurances of v2
                elif v2 > v1 + k:
                    temp += v2 - (v1 + k) # delete part of occurances of v1
            deletions = min(deletions, temp)
        return deletions
