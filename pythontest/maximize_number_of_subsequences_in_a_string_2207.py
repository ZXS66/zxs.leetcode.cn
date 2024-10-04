# https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/?envType=daily-question&envId=2024-09-24


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        head = pattern[0]
        tail = pattern[1]
        if head == tail:
            occurs = text.count(head)
            return occurs * (occurs + 1) // 2
        headCount = 0
        tailCount = 0
        for txt in text:
            if txt == head:
                headCount += 1
            elif txt == tail:
                tailCount += 1
        count = max(headCount, tailCount)
        for txt in text:
            if txt == head:
                count += tailCount
            elif txt == tail:
                tailCount -= 1
        return count

        # # 暴力破解法
        # maxCount = 0
        # head = pattern[0]
        # tail = pattern[1]
        # for i in range(len(text)):
        #     tmpTxt = text[0:i] + head + text[i:]
        #     count = self.calculate(tmpTxt, pattern)
        #     maxCount = max(maxCount, count)
        #     tmpTxt = text[0:i] + tail + text[i:]
        #     count = self.calculate(tmpTxt, pattern)
        #     maxCount = max(maxCount, count)
        # # do not forget the edge case: append head or tail to the end of the string
        # tmpTxt = text + head
        # count = self.calculate(tmpTxt, pattern)
        # maxCount = max(maxCount, count)
        # tmpTxt = text + tail
        # count = self.calculate(tmpTxt, pattern)
        # maxCount = max(maxCount, count)
        # return maxCount

    # def calculate(self, text: str, pattern: str) -> int:
    #     head = pattern[0]
    #     tail = pattern[1]
    #     count = 0
    #     for i in range(len(text) - 1):
    #         if text[i] == head:
    #             count += text.count(tail, i + 1)
    #     return count
