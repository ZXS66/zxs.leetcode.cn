# https://www.nowcoder.com/practice/b9eae162e02f4f928eac37d7699b352e?tpId=37&tqId=21251&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=

from typing import List

# to be optimized

class Solution:
    def max_pairs_of_prime_num(self, nums: List[int]) -> int:

        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        prime_pairs = []
        result = 0

        def search(nums:List[int]) -> int:
            n = len(nums)
            if n <= 1:
                return 0
            for i in range(n):
                for j in range(i + 1, n):
                    if is_prime(nums[i] + nums[j]):
                        prime_pairs.append((i, j))
                        sub = search(nums[0:i]+nums[i+1:j]+nums[j+1:])
                        return sub+1                 
            # 一个数字只能使用一次。
            return 1
        return len(prime_pairs)
