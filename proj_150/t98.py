# 题目：127.单词接龙
# 标签：BFS 哈希 字符串
# 难度：困难
# 日期：12.24

from typing import *
from collections import deque, defaultdict
from math import inf

# 思路:
# 和 t97 433.最小基因变化 相同 只差一个字母的 word 形成边 BFS

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbors = {word:[] for word in wordList}
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                word1, word2 = wordList[i], wordList[j]
                if self.is_neighbor(word1, word2):
                    neighbors[word1].append(word2)
                    neighbors[word2].append(word1)
        if endWord in neighbors:
            if beginWord not in neighbors:
                neighbors[beginWord] = []
                for word in wordList:
                    if self.is_neighbor(beginWord, word):
                        neighbors[beginWord].append(word)
                        neighbors[word].append(beginWord)
            vis = set([beginWord])
            q = deque([(beginWord, 1)])
            while q:
                word, step = q.popleft()
                for nxtword in neighbors[word]:
                    if nxtword == endWord:
                        return step + 1
                    elif nxtword not in vis:
                        vis.add(nxtword)
                        q.append((nxtword, step + 1))
        return 0

    def is_neighbor(self, word1:str, word2:str) -> bool:
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
                if diff > 1: return False
        return True

    def test(self):
        """test code
        """
        test_cases = [
            {
                "Input ": [],
                "Expect": [],
                "Output": []
            }
        ]
        for i, case in enumerate(test_cases):
            case["Output"].append(case["Input "]) # 调用求解
            print(f"Test {i + 1}")
            for key, val in case.items():
                print(f"\t\t{key}: {val}")

# 官方题解
# 双向BFS + 虚拟节点 hit -> *it h*t hi*
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1
        
        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)): # 链接到虚拟节点
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp
        
        wordId = dict()
        edge = defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)
        
        addEdge(beginWord)
        if endWord not in wordId:
            return 0
        
        disBegin = [inf for _ in range(nodeNum)]
        beginId = wordId[beginWord]
        disBegin[beginId] = 0
        queBegin = deque([beginId])

        disEnd = [inf for _ in range(nodeNum)]
        endId = wordId[endWord]
        disEnd[endId] = 0
        queEnd = deque([endId])

        while queBegin or queEnd:
            # 正向
            queBeginSize = len(queBegin)
            for _ in range(queBeginSize):
                nodeBegin = queBegin.popleft()
                if disEnd[nodeBegin] != inf: # 交汇
                    return (disBegin[nodeBegin] + disEnd[nodeBegin]) // 2 + 1
                for it in edge[nodeBegin]:
                    if disBegin[it] == inf: # 还未访问
                        disBegin[it] = disBegin[nodeBegin] + 1
                        queBegin.append(it)
            # 反向
            queEndSize = len(queEnd)
            for _ in range(queEndSize):
                nodeEnd = queEnd.popleft()
                if disBegin[nodeEnd] != inf:
                    return (disBegin[nodeEnd] + disEnd[nodeEnd]) // 2 + 1
                for it in edge[nodeEnd]:
                    if disEnd[it] == inf:
                        disEnd[it] = disEnd[nodeEnd] + 1
                        queEnd.append(it)
        return 0


# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()