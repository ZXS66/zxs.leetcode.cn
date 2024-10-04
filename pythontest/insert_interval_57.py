# https://leetcode.cn/problems/insert-interval/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if intervals is None or len(intervals) == 0: return [newInterval]
        # edge case: newInterval is the smallest
        if newInterval[1]<intervals[0][0]: return [newInterval]+intervals
        # edge case: newInterval is the largest
        if newInterval[0]>intervals[-1][1]: return intervals+[newInterval]
        res = []
        n = len(intervals)
        i = 0
        while i<n:
            v = intervals[i]
            if len(res)>0 and res[-1][0]>=v[0] and res[-1][1]<=v[1]:
                # overlap
                continue
            elif v[1]<newInterval[0]:
                # the interval is smaller than newInterval
                res.append(v)
            elif v[0]>newInterval[1] and len(res)>0 and newInterval[0]>res[-1][1]:
                res.append(newInterval)
                i-=1
            elif v[0]>newInterval[1] and len(res)>0 and v[0]>res[-1][1]:
                # the interval is larger than newInterval
                res.append(v)
            else:
                newStart = min(v[0],newInterval[0])
                newEnd = max(v[1],newInterval[1])
                if len(res)>0 and res[-1][1]>=newStart:
                    res[-1][1] = newEnd
                else:
                    res.append([newStart,newEnd])
            i+=1
        return res
