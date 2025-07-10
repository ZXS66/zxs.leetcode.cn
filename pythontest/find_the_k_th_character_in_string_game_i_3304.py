# https://leetcode.cn/problems/find-the-k-th-character-in-string-game-i/?envType=daily-question&envId=2025-07-03

from string import ascii_lowercase


class Solution:
    def kthCharacter(self, k: int) -> str:
        # approach 1: bit count
        # return ascii_lowercase[(k - 1).bit_count()]

        # approach 2: mutate the string as required
        # cache = [97]
        # while len(cache) < k:
        #     # 97 is 'a', 122 is 'z'
        #     cache += [97 if i == 122 else i + 1 for i in cache]
        # return chr(cache[k - 1])
    
        # approach 3: precomputed cache
        cache = 'abbcbccdbccdcddebccdcddecddedeefbccdcddecddedeefcddedeefdeefeffgbccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghbccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghcddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhibccdcddecddedeefcddedeefdeefeffgcddedeefdeefeffgdeefeffgeffgfgghcddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhicddedeefdeefeffgdeefeffgeffgfgghdeefeffgeffgfggheffgfgghfgghghhideefeffgeffgfggheffgfgghfgghghhieffgfgghfgghghhifggh'
        return cache[k - 1]
