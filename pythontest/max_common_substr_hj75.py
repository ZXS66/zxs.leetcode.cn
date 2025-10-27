# https://www.nowcoder.com/practice/98dc82c094e043ccb7e0570e5342dd1b?tpId=37&tqId=21298&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=


class Solution:
    def max_common_substr(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)

        # make sure t's length is always greater than s
        if ls > lt:
            s, t = t, s
            ls, lt = lt, ls

        visited = set()
        result = ls
        found=False
        while result > 0:
            for i in range(ls - result + 1):
                val = s[i : result + i]
                if val in visited:
                    continue
                visited.add(val)
                if val in t:
                    found = True
                    break
            if found:
                break
            result = result - 1

        return result
