# https://leetcode.cn/problems/word-ladder/description/?envType=study-plan-v2&envId=top-interview-150

from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if beginWord == endWord:
            return 1
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        mutations = "abcdefghijklmnopqrstuvwxyz"
        queue = deque([(beginWord, 1)])
        while queue:
            word, mutate = queue.popleft()
            for i in range(len(word)):
                for m in mutations:
                    newWord = word[:i] + m + word[i + 1 :]
                    if newWord != word and newWord in wordList:
                        if newWord == endWord:
                            return mutate + 1
                        wordList.remove(newWord)
                        queue.append((newWord, mutate + 1))
        return 0
