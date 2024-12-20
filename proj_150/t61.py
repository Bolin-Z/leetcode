# 题目：92.反转链表II
# 标签：链表
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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_pre, left_ptr = None, head
        for _ in range(left - 1):
            left_pre = left_ptr
            left_ptr = left_ptr.next
        cur, last = left_ptr, left_pre
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = last
            last = cur
            cur = nxt
        right_ptr, right_nxt = last, cur
        left_ptr.next = right_nxt
        if left_pre:
            left_pre.next = right_ptr
            return head
        else:
            return right_ptr
    
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
# 灵山
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p0 = dummy = ListNode(next=head)
        for _ in range(left - 1):
            p0 = p0.next
        pre, cur = None, p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        # cur 为翻转最右的节点的下一个
        # pre 为翻转的最右节点
        # p0 为翻转的最左节点的前一个
        # p0.next 为翻转的最左节点
        p0.next.next = cur
        p0.next = pre
        return dummy.next

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()