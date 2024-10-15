# https://leetcode.cn/problems/maximum-height-of-a-triangle/

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        if red == 1 and blue == 1: return 1
        elif red == 1 or blue == 1: return 2
        if red < blue:
            # make sure red is the greater one
            red, blue = blue, red
        def triangleNodes(height:int):
            """分别返回奇数行节点数总和和偶数行节点数总和"""
            # 等差数列求和公式：n / 2 * (a1 + an)
            if height % 2 == 0: return height / 4 * height, height / 4 * (2 + height) # 偶数
            else: return (height+1)/4*(1+height), (height-1)/4*(1+height) # 奇数
        
        ans = 2
        while True:
            odd, even = triangleNodes(ans)
            if ans % 2 == 0:
                # even is greater than odd
                if even > red or odd > blue: return ans - 1
            else:
                # odd is greater than even
                if odd > red or even > blue: return ans - 1
            ans += 1
        
        # 也可以从 red 和 blue 中取一个作为底边，然后求出最大高度，最多计算四次
