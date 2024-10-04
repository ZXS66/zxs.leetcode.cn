# https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ans = 1
        pre = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > pre:
                ans += 1
                pre = points[i][1]
        return ans
