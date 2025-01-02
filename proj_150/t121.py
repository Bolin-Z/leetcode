# 题目：215.数组中的第K个最大元素
# 标签：数组 分治 快速选择 排序 堆(优先队列)
# 难度：中等
# 日期：1.1

from typing import *

# 思路:
#

from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res = None
        s = len(nums) - k + 1
        for _ in range(s):
            res = heappop(nums)
        return res

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
# 自己实现一个二叉堆
# 完全二叉树: 只允许最后一排不满，且最后一行必须从左往右排序，最后一行元素之间不可以有间隔

# 两个操作：上滤(上浮) 下滤(下沉)
# 建堆:自顶向下、自底向上


# 从 0 开始 下标为 i 的子节点为 2*i + 1 和 2*i + 2
# i 的父节点为 floor((i - 1) / 2) 即 (i - 1) // 2
# 最小堆
class Heap:

    def __init__(self, nums:List[int]=None) -> None:
        if nums is None:
            nums = []
        self.heap_size = len(nums)
        self.heap_list = nums
        self.heapify(nums)
    
    def insert(self, k:int) -> None:
        self.heap_list.append(k)
        self.heap_size += 1
        self._precUp(self.heap_size - 1)
    
    def findMin(self) -> Optional[int]:
        return None if self.isEmpty() else self.heap_list[0]
    
    def delMin(self) -> Optional[int]:
        if self.isEmpty():
            return None
        min_val = self.heap_list[0]
        self.heap_list[0] = self.heap_list[-1]
        self.heap_list.pop()
        self.heap_size -= 1
        self._precDown(0)
        return min_val

    def isEmpty(self) -> bool:
        return self.heap_size == 0

    def heapify(self, nums:List[int]) -> None:
        # 从列表构建最小堆
        if nums is not self.heap_list:
            self.heap_list = nums
            self.heap_size = len(nums)
        last_parent = ((self.heap_size - 1) - 1) // 2 # 最后一个父节点
        while last_parent >= 0:
            self._precDown(last_parent)
            last_parent -= 1

    def _precUp(self, idx:int) -> None:
        parent_idx = (idx - 1) // 2
        while parent_idx > -1: # 父节点存在
            if self.heap_list[parent_idx] <= self.heap_list[idx]: # 满足堆性质
                break
            # 不满足堆性质
            self.heap_list[idx], self.heap_list[parent_idx] = self.heap_list[parent_idx], self.heap_list[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def _precDown(self, idx:int) -> None:
        left_child, right_child = idx * 2 + 1, idx * 2 + 2
        while left_child < self.heap_size: # 非叶子节点
            min_idx = self._min_child(left_child, right_child)
            if self.heap_list[idx] <= self.heap_list[min_idx]: # 满足堆性质
                break
            self.heap_list[idx], self.heap_list[min_idx] = self.heap_list[min_idx], self.heap_list[idx]
            idx = min_idx
            left_child, right_child = idx * 2 + 1, idx * 2 + 2

    def _min_child(self, left:int, right:int) -> int:
        if not right < self.heap_size: # 没有右子节点
            return left
        else:
            return left if self.heap_list[left] < self.heap_list[right] else right

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        priorityq = Heap(nums)
        ans = None
        for _ in range(len(nums) - k + 1):
            ans = priorityq.delMin()
        return ans


# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()