# https://leetcode.cn/problems/minimum-time-to-complete-trips/solutions/1300957/wan-cheng-lu-tu-de-zui-shao-shi-jian-by-uxyrp/

class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        if len(time) == 1: return time[0] * totalTrips
        left, right = min(time), min(time) * totalTrips
        while left < right:
            mid = (left + right) // 2
            if sum(mid // t for t in time) >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return left