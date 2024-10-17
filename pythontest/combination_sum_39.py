# https://leetcode.cn/problems/combination-sum/description/?envType=study-plan-v2&envId=top-interview-150

from collections import Counter

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        res_counter = []
        def backtrack(combine, target):
            if target < 0:
                # 2 <= candidates[i] <= 40
                return
            if target == 0:
                # 如果至少一个数字的被选数量不同，则两种组合是不同的。
                ctr = Counter(combine)
                if ctr not in res_counter:
                    res_counter.append(ctr)
                    res.append(combine)
                return
            for i in range(len(candidates)):
                # candidates 中的 同一个 数字可以 无限制重复被选取
                backtrack(combine + [candidates[i]], target - candidates[i])
    
        backtrack([], target)
        return res
