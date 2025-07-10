# https://leetcode.cn/problems/partition-labels/description/?envType=study-plan-v2&envId=top-100-liked

from typing import List
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = defaultdict(int)
        for i, char in enumerate(s):
            last_occurrence[char] = i

        partitions = []
        start, end = 0, 0
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:
                partitions.append(end - start + 1)
                start = end + 1

        return partitions
