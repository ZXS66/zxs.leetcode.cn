# https://www.nowcoder.com/practice/98dc82c094e043ccb7e0570e5342dd1b?tpId=37&tqId=21298&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=


class Solution:
    def max_bits(self, n:int) -> int:
        nstr=bin(int(n))[2:]

        result,idx=0,-1
        for i in range(len(nstr)):
            if nstr[i]=='0':
                idx=i
            result=max(result, i-idx)

        return result
