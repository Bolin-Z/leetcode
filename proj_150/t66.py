# 题目：86.分隔链表
# 标签：链表 双指针
# 难度：中等
# 日期：12.19

from typing import *

# 思路:
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next:'Optional[ListNode]'=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_tail = less_head = ListNode()
        great_tail = great_head = ListNode()
        cur = head
        while cur:
            if cur.val < x:
                less_tail.next = cur
                less_tail = less_tail.next
            else:
                great_tail.next = cur
                great_tail = great_tail.next
            cur = cur.next
        less_tail.next = great_head.next
        great_tail.next = None
        return less_head.next
        
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