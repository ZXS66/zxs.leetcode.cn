# https://leetcode.cn/problems/basic-calculator/description/?envType=study-plan-v2&envId=top-interview-150

"""
基本计算器
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

 

示例 1：

输入：s = "1 + 1"
输出：2
示例 2：

输入：s = " 2-1 + 2 "
输出：3
示例 3：

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
 

提示：

1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式
'+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
'-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
输入中不存在两个连续的操作符
每个数字和运行的计算将适合于一个有符号的 32位 整数

"""

import re


class Solution:
    def __init__(self) -> None:
        self.__digits = [str(i) for i in range(10)]

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        while True:
            match = re.search(r"\(([^()]+)\)", s)
            if match is None:
                break
            else:
                s = s.replace(
                    match.group(0), str(self._simple_calculate(match.group(1)))
                )
                # bug fix: partial result could be negative integer
                s = s.replace("--", "+").replace("+-", "-")
        return self._simple_calculate(s)

    def _simple_calculate(self, s: str) -> int:
        """calculate without parentheses"""
        segments = []
        for i in range(len(s)):
            if s[i] in ("+", "-", "(", ")"):
                segments.append(s[i])
            elif s[i] in self.__digits:
                if s[i - 1] in self.__digits and len(segments) > 0:
                    segments[-1] += s[i]
                else:
                    segments.append(s[i])
        if segments[0] in ("+", "-"):
            # consider positive or negative sign for the first digit
            segments = ["0"] + segments
        if len(segments) == 1:
            return int(segments[0])
        stack = segments[0:2]
        for i in range(2, len(segments)):
            seg = segments[i]
            if seg in ("+", "-"):
                stack.append(seg)
            else:
                op = stack.pop()
                if op == "+":
                    stack[0] = int(stack[0]) + int(seg)
                else:
                    stack[0] = int(stack[0]) - int(seg)
        return stack[0]
