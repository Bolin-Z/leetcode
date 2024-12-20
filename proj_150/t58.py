# 题目：2.两数相加
# 标签：递归 链表 数学
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, tail = None, None
        carry_bit = 0
        num1, num2 = l1, l2
        while num1 and num2:
            res = ListNode()
            carry_bit, res.val = divmod(num1.val + num2.val + carry_bit, 10)
            num1, num2 = num1.next, num2.next
            if not head: head = tail = res
            else:
                tail.next = res
                tail = res
        num = num1 if num1 else num2
        while num:
            res = ListNode()
            carry_bit, res.val = divmod(num.val + carry_bit, 10)
            num = num.next
            tail.next = res
            tail = res
        if carry_bit:
            tail.next = ListNode(val=1)
        return head


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
# 灵山 使用递归的思想，循环实现
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode() # 哨兵
        carry = 0 # 进位
        while l1 or l2 or carry: # 需要创建节点
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode()
            carry, cur.next.val = divmod(carry, 10)
            cur = cur.next
        return dummy.next

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()