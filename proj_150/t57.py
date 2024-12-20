# 题目：141.环形链表
# 标签：哈希 链表 双指针
# 难度：简单
# 日期：12.19

from typing import *

# 思路:
# 快慢指针秒了

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     fast = slow = head
    #     while fast and slow:
    #         fast = fast.next
    #         if not fast: return False
    #         else:
    #             fast = fast.next
    #         slow = slow.next
    #         if fast == slow:
    #             return True
    #     return False
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False

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

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()