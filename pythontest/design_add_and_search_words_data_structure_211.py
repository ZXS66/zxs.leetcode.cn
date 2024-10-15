# https://leetcode.cn/problems/design-add-and-search-words-data-structure/description/?envType=study-plan-v2&envId=top-interview-150

# 参考 [问题208](https://leetcode.cn/problems/implement-trie-prefix-tree/description/)

from collections import Counter, defaultdict

class WordDictionary:

    def __init__(self):
        self.dictw = {}
        self.dictn = defaultdict(list)

    def addWord(self, word: str) -> None:
        if word not in self.dictw:
            self.dictn[len(word)].append(word)
            self.dictw[word] = len(word)

    def search(self, word: str) -> bool:
        if word in self.dictw:
            return True
        # 双dict，长度和字符互相为key，直接比较，完美
        for w in self.dictn[len(word)]:
            if '.' in word:
                length = 0
                for i in range(len(w)):
                    if w[i] == word[i] or word[i] == '.':
                        length += 1
                    else:
                        break
                if length == len(w):
                    return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)