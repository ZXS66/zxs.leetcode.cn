# https://leetcode.cn/problems/find-the-k-th-character-in-string-game-ii/description/?envType=daily-question&envId=2025-07-04

from string import ascii_lowercase
from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # approach 1: timeout!!
        # word = [97]  # 'a'
        # for op in operations:
        #     if op == 0:
        #         word += word
        #     else:
        #         word += [97 if ch == 122 else ch + 1 for ch in word]

        # return chr(word[k - 1])

        # approach 2: also timeout!!!
        # word = [0]
        # for op in operations:
        #     if op == 0:
        #         word += word
        #     else:
        #         word += [0 if ch == 25 else ch + 1 for ch in word]
        # return ascii_lowercase[word[k - 1]]

        # approach 3: time limit exceeded
        # mutation = {"a":"b","b":"c","c":"d","d":"e","e":"f","f":"g","g":"h","h":"i","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t","t":"u","u":"v","v":"w","w":"x","x":"y","y":"z","z":"a"}
        # word = ["a"]
        # for op in operations:
        #     if len(word) >= k:
        #         break
        #     if op == 0:
        #         word += word
        #     else:
        #         word += [mutation[ch] for ch in word]
        # return word[k - 1]

        ans = 0
        k -= 1
        for i in range(k.bit_length() - 1, -1, -1):
            if (k >> i) & 1:
                ans += operations[i]
        return chr(ord('a') + (ans % 26))