# https://leetcode.cn/problems/word-search-ii/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class TrieNode:
    """字典树节点"""

    def __init__(self):
        self.children = {}  # 子节点列表
        self.str = ""  # 如果是尾节点，存储对应的单词


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res = []

        def insert(word: str):
            """将单词`word`插入字段数`root`"""
            node = self.root  # 从根节点开始构造这个word对应的路径节点
            for ch in word:
                if ch not in node.children:
                    # 字符ch对应的节点不存在，新建一个
                    node.children[ch] = TrieNode()
                # 更新node
                node = node.children[ch]
            node.str = word  # 尾节点记录单词，用于后序查找的时候快速得到

        # 构建words的字典树
        self.root = TrieNode()  # 根节点
        for word in words:
            if len(word) > m * n:
                continue  # 字符串长度超过二维矩阵尺寸，肯定无法构成
            insert(word)

        def dfs_Search(
            board: List[List[str]], r: int, c: int, node: "TrieNode", len_: int
        ):
            """
            深度优先搜索的同时，判断当前路径构成的字符串是否为查找单词
            @param board: 二维网格
            @param r: 行号
            @param c: 列号
            @param node：当前字符对应的路径节点
            @param len_: 当前路径构成的字符串长度
            @param res：结果集
            """
            if len_ > 10:
                return  # 字符串长度超过10，返回
            ch = board[r][c]  # 获取当前行列对应的字符
            if ch not in node.children:
                return  # 当前字符对应的节点不存在，即构造的字符串不在words中
            last = node  # 记录当前node
            node = node.children[ch]  # 更新当前node为当前字符对应得到的节点
            if node.str:
                res.append(
                    node.str
                )  # 当前节点记录了一个单词，则得到了一个words中的单词
                node.str = ""  # 匹配了单词，不重复匹配
            if not node.children:
                # 当前节点没有后序字符了，那么这个节点一定是某个单词最后一个字符对应的节点。
                # 并且不是其他任何单词的前缀，因此匹配完了之后，可以将这个字符从其父节点的childran列表中删除。
                last.children.pop(ch)
                return
            len_ += 1  # 更新长度
            board[r][c] = "*"  # 用特殊符号标记当前位置已使用
            # 四个方向转递递归
            if r - 1 >= 0 and board[r - 1][c] != "*":
                dfs_Search(board, r - 1, c, node, len_)
            if r + 1 < len(board) and board[r + 1][c] != "*":
                dfs_Search(board, r + 1, c, node, len_)
            if c - 1 >= 0 and board[r][c - 1] != "*":
                dfs_Search(board, r, c - 1, node, len_)
            if c + 1 < len(board[0]) and board[r][c + 1] != "*":
                dfs_Search(board, r, c + 1, node, len_)
            board[r][c] = ch  # 回溯，这个位置处理完了恢复成原来的字符

        # 以二维网格的每个位置(i,j)为起点，寻找以其为首字符的所有字符串
        for i, row in enumerate(board):
            for j, _ in enumerate(row):
                dfs_Search(board, i, j, self.root, 0)

        return res


# 作者：画图小匠
# 链接：https://leetcode.cn/problems/word-search-ii/solutions/1/javapython3chui-su-fa-zi-dian-shu-jian-z-0o8a/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
