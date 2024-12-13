# 题目：238. 除自身以外数组的乘积
# 标签：数组 前缀和
# 难度：中等

from typing import *

# 思路:
# 假设有两个数组 pre[i] suf[i]
# pre[i] 表示从第 0 个数乘到第 i 个数
# suf[i] 表示从第 i 个数乘到第 n - 1 个数
# answer[i] = pre[i - 1] * suf[i + 1]

class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     total_nums = len(nums)
    #     pre = [1 for _ in range(total_nums + 1)]
    #     suf = [1 for _ in range(total_nums + 1)]
    #     for i in range(total_nums):
    #         pre[i + 1] = pre[i] * nums[i]
    #     for i in range(total_nums - 1, -1, -1):
    #         suf[i] = suf[i + 1] * nums[i]
    #     ans = []
    #     for i in range(total_nums):
    #         ans.append(pre[i] * suf[i + 1])
    #     return ans

    # 不需要额外空间解法，ans先计算前缀乘积，做后缀乘积的时候直接更新为正确答案
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     total_nums = len(nums)
    #     ans = []
    #     prod = 1
    #     for i in range(total_nums):
    #         prod *= nums[i]
    #         ans.append(prod)
    #     prod = 1
    #     for i in range(total_nums - 1, 0, -1):
    #         ans[i] = ans[i - 1] * prod
    #         prod *= nums[i]
    #     ans[0] = prod
    #     return ans
    
    # 使用双指针
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in range(len(nums))]
        left, right = 0, len(nums) - 1
        left_prod, right_prod = 1, 1
        while left < len(nums) and right >= 0:
            answer[right] *= right_prod
            answer[left] *= left_prod
            right_prod *= nums[right]
            left_prod *= nums[left]
            right -= 1
            left += 1
        return answer


    def test(self):
        """test code
        """
        test_cases = []
        pass

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()