# 题目：46.全排列
# 标签：数组 回溯
# 难度：中等
# 日期：12.25

from typing import *

# 思路:
#

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        per = []
        ans = []
        n = len(nums)
        def dfs(idx:int) -> None:
            if idx < n:
                candidate = [num for num in nums if num not in per]
                for num in candidate:
                    per.append(num)
                    dfs(idx + 1)
                    per.pop()
            else:
                ans.append(per.copy())
        dfs(0)
        return ans

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
# 节省空间的写法，原地修改nums数组，将使用过的数字放到左侧，未使用在右侧
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def dfs(idx:int) -> None:
            if idx < n:
                for pos in range(idx, n):
                    nums[idx], nums[pos] = nums[pos], nums[idx] # 交换
                    dfs(idx + 1)
                    nums[idx], nums[pos] = nums[pos], nums[idx] # 换回来
            else:
                ans.append(nums.copy())
        dfs(0)
        return ans


# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()