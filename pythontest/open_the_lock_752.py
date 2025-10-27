# https://leetcode.cn/problems/open-the-lock/description/

from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if '0000' in dead_set:
            return -1
        
        def neighbors(node: str) -> List[str]:
            res = []
            for i in range(4):
                digit = int(node[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_node = node[:i] + str(new_digit) + node[i+1:]
                    res.append(new_node)
            return res
        
        queue = deque([('0000', 0)])
        visited = {'0000'}
        
        while queue:
            node, steps = queue.popleft()
            if node == target:
                return steps
            for neighbor in neighbors(node):
                if neighbor not in dead_set and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        
        return -1
        
