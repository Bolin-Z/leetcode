# 题目：25.K个一组翻转链表
# 标签：递归 链表
# 难度：困难
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        left_pre, right, cur = dummy, None, dummy.next
        cnt = 0
        while cur:
            cnt += 1
            if cnt == k:
                left, right = left_pre.next, cur
                self.reverseK(left, right, k)
                cur = left
                left_pre.next = right
                left_pre = left
                cnt = 0
            cur = cur.next
        return dummy.next

# 灵山
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
    
    def reverseK(self, left: Optional[ListNode], right: Optional[ListNode], k: int) -> None:
        cur, last = left, right.next
        for _ in range(k):
            nxt = cur.next
            cur.next = last
            last = cur
            cur = nxt

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