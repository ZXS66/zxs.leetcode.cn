# https://leetcode.cn/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        if num in roman_map:
            return roman_map[num]
        segments = list()
        for key, val in roman_map.items():
            while num >= key:
                num -= key
                segments.append(val)
            if num == 0:
                break
        return "".join(segments)
