# https://leetcode.cn/problems/super-egg-drop/description/

# similar to [1884](https://leetcode.cn/problems/egg-drop-with-2-eggs-and-n-floors/description/)

from functools import cache


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # 注意边界条件：0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
        # 共 n+1 种情况，最差需要 n 次操作
        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 x values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(k, n)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/super-egg-drop/solutions/197163/ji-dan-diao-luo-by-leetcode-solution-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。