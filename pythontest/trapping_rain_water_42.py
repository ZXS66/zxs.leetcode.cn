# https://leetcode.cn/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        while left < right:
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)
            if leftMax < rightMax:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans
