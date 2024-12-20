# 题目：61.旋转链表
# 标签：链表 双指针
# 难度：中等
# 日期：12.19

from typing import *

# 思路:
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return head
        cur = fake_head = ListNode(next=head)
        len_of_list = 0
        while cur.next:
            len_of_list += 1
            cur = cur.next
        tail = cur
        tail.next = fake_head.next
        k %= len_of_list
        cur = fake_head
        for _ in range(len_of_list - k):
            cur = cur.next
        fake_head.next = cur.next
        cur.next = None
        return fake_head.next

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