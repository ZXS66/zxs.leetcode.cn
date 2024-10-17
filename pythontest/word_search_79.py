# https://leetcode.cn/problems/word-search/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i:int, j:int, k:int, trace:str) -> bool:
            if k == len(word) - 1:
                return True
            new_trace = trace + f'[{i},{j}]'
            # if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k] or footprint in trace:
            #     return False
            # return dfs(i + 1, j, k + 1, new_trace) or dfs(i - 1, j, k + 1, new_trace) or dfs(i, j + 1, k + 1, new_trace) or dfs(i, j - 1, k + 1, new_trace)
            # 更快剪枝 version
            if (i+1)<m and board[i+1][j]==word[k+1] and f'[{i+1},{j}]' not in trace and dfs(i+1, j, k+1, new_trace):
                return True
            elif (i-1)>=0 and board[i-1][j]==word[k+1] and f'[{i-1},{j}]' not in trace and dfs(i-1, j, k+1, new_trace):
                return True
            elif (j+1)<n and board[i][j+1]==word[k+1] and f'[{i},{j+1}]' not in trace and dfs(i, j+1, k+1, new_trace):
                return True
            elif (j-1)>=0 and board[i][j-1]==word[k+1] and f'[{i},{j-1}]' not in trace and dfs(i, j-1, k+1, new_trace):
                return True
            else:
                return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]: 
                    continue
                if dfs(i, j, 0, ""):
                    return True
        
        return False