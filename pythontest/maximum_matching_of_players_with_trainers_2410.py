# https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/description/?envType=daily-question&envId=2025-07-13

from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = 0, 0
        matches = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                matches += 1
                i += 1
            j += 1
        return matches
