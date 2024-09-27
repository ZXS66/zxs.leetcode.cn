# https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = [0] * 3

        for c in s:
            cnt[ord(c) - ord('a')] += 1
        if cnt[0] < k or cnt[1] < k or cnt[2] < k:
            return -1

        ans = len(s)
        l = 0
        for r, ch in enumerate(s):
            cnt[ord(ch) - ord('a')] -= 1
            while l < r and (cnt[0] < k or cnt[1] < k or cnt[2] < k):
                cnt[ord(s[l]) - ord('a')] += 1
                l += 1
            if cnt[0] >= k and cnt[1] >= k and cnt[2] >= k:
                ans = min(ans, len(s) - (r - l + 1))

        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/solutions/2928177/mei-chong-zi-fu-zhi-shao-qu-k-ge-by-leet-10ct/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

