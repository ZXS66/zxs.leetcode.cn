# https://leetcode.cn/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]: 
                if ans[-1][1] < intervals[i][1]:
                    ans[-1][1] = intervals[i][1]
            else:
                ans.append(intervals[i])
        return ans
