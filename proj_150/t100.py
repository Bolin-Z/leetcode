# 题目：212.单词搜索II *
# 标签：字典树 数组 字符串 回溯 矩阵
# 难度：困难
# 日期：12.25

from typing import *
from collections import *

# 思路:
# 字典树 + DFS回溯法

class TreeNode:
    def __init__(self, isword:bool=False) -> None:
        self.isword = isword
        self.childs:Dict[str, TreeNode] = {}

class Tries:
    def __init__(self) -> None:
        self.root = TreeNode(False)
    
    def insert(self, word:str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.childs:
                ptr.childs[c] = TreeNode(False)
            ptr = ptr.childs[c]
        ptr.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words_tries = Tries()
        m, n = len(board), len(board[0])
        for word in words:
            words_tries.insert(word)
        ans = set()
        visited = set()
        def dfs(x:int, y:int, node:TreeNode, prefix:str) -> None:
            nonlocal ans, visited
            if not (0 <= x < m and 0 <= y < n) or (x, y) in visited:
                return
            c = board[x][y]
            if c in node.childs:
                new_prefix = prefix + c
                new_node = node.childs[c]
                if new_node.isword:
                    ans.add(new_prefix)
                visited.add((x,y))
                dfs(x, y + 1, new_node, new_prefix)
                dfs(x, y - 1, new_node, new_prefix)
                dfs(x + 1, y, new_node, new_prefix)
                dfs(x - 1, y, new_node, new_prefix)
                visited.discard((x,y))
        for x in range(m):
            for y in range(n):
                dfs(x, y, words_tries.root, "")
        return list(ans)

    def test(self):
        board = [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ]
        words = ["oath","pea","eat","rain"]
        ans = self.findWords(board, words)

# 官方题解
# Trie树简洁写法 + 结点直接存储字符串 + 删除已找到的单词剪枝
from collections import defaultdict

class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.word = ""
        self.is_word = False

    def insert(self, word):
        ptr = self
        for c in word:
            ptr = ptr.children[c] # 使用了defaultdict会自动创建
        ptr.is_word = True
        ptr.word = word # 大量相同前缀不知道会不会爆

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def dfs(now:Trie, x:int, y:int):
            nonlocal ans, m, n
            ch = board[x][y]
            if ch not in now.children:
                return
            nxt_node = now.children[ch]
            if nxt_node.word != "":
                ans.append(nxt_node.word)
                nxt_node.word = "" # 剪掉
            if nxt_node.children: # 如果有子代
                board[x][y] = "#" # 标记 相当于 visit
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < m and 0 <= ny < n:
                        dfs(nxt_node, nx, ny)
                board[x][y] = ch # 回溯
            
            # 因为如果有以 ch 为结尾的单词 如果能匹配已经匹配完了
            # 其没有子代，所以就可以不用匹配到 ch 之后了
            if not nxt_node.children: # 为什么？
                now.children.pop(ch)
        
        ans = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)
        return ans

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()