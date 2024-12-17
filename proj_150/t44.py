# 题目：1.两数之和
# 标签：
# 难度：简单
# 日期：12.17

from typing import *

# 思路:
# 形成 (val, idx) 对数组
# 排序 + 双指针 (麻烦了

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = sorted([(val, idx) for idx, val in enumerate(nums)], key=lambda t:t[0])
        ans = []
        left, right = 0, len(val_idx) - 1
        while left < right:
            sum = val_idx[left][0] + val_idx[right][0]
            if sum == target:
                ans.extend([val_idx[left][1], val_idx[right][1]])
                break
            elif sum < target:
                left += 1
            else:
                right -= 1
        return ans

    def test(self):
        """test code
        """
        test_cases = []
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = []
            if type(answer) == List:
                for ans in answer:
                    print(f"\t\t{ans}")
            else:
                print(f"\t\t{answer}")

# 官方题解
# 使用一个哈希表记录出现过的数值和下标
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i, x in enumerate(nums):
            if target - x in found:
                return [found[target - x], i]
            else:
                found[x] = i
        return []


# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()