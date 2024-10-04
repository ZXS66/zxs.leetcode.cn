# https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150

"""
最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109

"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        maxDistance = 0
        currentDistance = 0
        for num in nums:
            if num - 1 not in nums:
                currentNum = num
                currentDistance = 1
                while currentNum + 1 in nums:
                    currentNum += 1
                    currentDistance += 1
                maxDistance = max(maxDistance, currentDistance)
        return maxDistance
        