# https://leetcode.cn/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def romanToInt(self, s: str) -> int:
        # roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # edgeCases = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        # tmp = s
        # for ec in edgeCases:
        #     if ec in tmp:
        #         tmp = tmp.replace(ec, f"_{edgeCases[ec]}_")
        # for item in roman_dict:
        #     tmp = tmp.replace(item, f"_{roman_dict[item]}_")
        # nums = [int(i) for i in tmp.split("_") if i != ""]
        # return sum(nums)
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ret = 0
        n = len(s)
        for idx, val in enumerate(s):
            numVal = roman_dict[val]
            if idx < n - 1 and numVal < roman_dict[s[idx + 1]]:
                ret -= numVal
            else:
                ret += numVal
        return ret
