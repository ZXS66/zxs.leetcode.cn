# https://leetcode.cn/problems/combinations/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        path = []
        def backtrack(start: int):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)  # 向路径中添加一个元素
                backtrack(i + 1)
                path.pop()  # 回溯，撤销选择
        backtrack(1)
        return res
