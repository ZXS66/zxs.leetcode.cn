# https://www.nowcoder.com/practice/98dc82c094e043ccb7e0570e5342dd1b?tpId=37&tqId=21298&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=



from collections import deque


class Solution:
    def max_echo_substr(self, s: str) -> int:
        ls= len(s)
        result = 0
        for i in range(ls):
            for j in range(i + 1, ls + 1):
                if s[i:j] == s[i:j][::-1]:
                    result = max(result, j - i)
        return result

        # stack = deque()
        # result = 0
        # for ch in s:
        #     stack.append(ch)
        #     temp = ''
        #     for i in range(len(stack) - 1, -1, -1):
        #         temp = stack[i] + temp
        #         if temp == s[len(stack) - len(temp) : len(stack)]:
        #             result = max(result, len(temp))
        # return result