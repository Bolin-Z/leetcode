# 题目：71.简化路径
# 标签：
# 难度：
# 日期：12.18

from typing import *

# 思路:
#

class Solution:
    def simplifyPath(self, path: str) -> str:
        patt = path.split("/")
        stack = []
        for p in patt:
            if p and p != ".":
                if p == ".." :
                    if stack:
                        stack.pop(-1)
                else:
                    stack.append(p)
        return "/" + "/".join(stack)
        # if len(stack) == 0: return "/"
        # else:
        #     ans = ""
        #     for p in stack:
        #         ans += "/" + p
        #     return ans

    def test(self):
        """test code
        """
        test_cases = [
            {
                "Input_": ["/home//foo/"],
                "Expect": [],
                "Output": []
            },
            {
                "Input_": ["/.../a/../b/c/../d/./"],
                "Expect": [],
                "Output": []
            }
        ]
        for i, case in enumerate(test_cases):
            case["Output"].append(self.simplifyPath(case["Input_"][0])) # 调用求解
            print(f"Test {i + 1}")
            for key, val in case.items():
                print(f"\t\t{key}: {val}")

# 官方题解

# 测试
if __name__ == "__main__":
    s = "/".join([])
    print(s)
    solver = Solution()
    solver.test()