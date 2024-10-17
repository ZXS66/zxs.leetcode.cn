# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        ans = []
        if not digits: return ans
        num_map: dict[str, str] = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def backtrack(index: int, path: str):
            if len(path) == len(digits):
                ans.append(path)
                return 
                # 遍历当前位置所有可能的字母
            for letter in num_map[digits[index]]:
                backtrack(index + 1, path + letter)
        backtrack(0, "")
        return ans
