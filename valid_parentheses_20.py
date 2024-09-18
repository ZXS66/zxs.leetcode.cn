# https://leetcode.cn/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150

"""
有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
 

示例 1：

输入：s = "()"

输出：true

示例 2：

输入：s = "()[]{}"

输出：true

示例 3：

输入：s = "(]"

输出：false

示例 4：

输入：s = "([])"

输出：true

 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == ")":
                    if stack[-1] != "(":
                        return False
                    stack.pop()
                elif i == "]":
                    if stack[-1] != "[":
                        return False
                    stack.pop()
                elif i == "}":
                    if stack[-1] != "{":
                        return False
                    stack.pop()
        return len(stack) == 0
