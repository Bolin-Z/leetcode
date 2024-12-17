# 题目：49.字母异位词分组
# 标签：数组 哈希 字符串 排序
# 难度：中等
# 日期：12.17

from typing import *

# 思路:
# 字母异位词是等价类
# 坑的点: 哈希表的键值设定需要不可变类型

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for word in strs:
            patt = "".join(sorted(word))
            if patt in hashtable:
                hashtable[patt].append(word)
            else:
                hashtable[patt] = [word]
        answer = [l for l in hashtable.values()]
        return answer

    def test(self):
        """test code
        """
        test_cases = [
            ["eat","tea","tan","ate","nat","bat"]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.groupAnagrams(case)
            if type(answer) == List:
                for ans in answer:
                    print(f"\t\t{ans}")
            else:
                print(f"\t\t{answer}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()