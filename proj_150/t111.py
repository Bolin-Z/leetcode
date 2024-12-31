# 题目：23. 合并k个升序链表
# 标签：链表 分治 堆(优先队列) 归并排序
# 难度：困难
# 日期：12.27

from typing import *

# 思路:
# 两两合并？

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        for list in lists:
            head = self.mergeTwoLists(head, list)
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
# 使用优先队列 灵
# 同时合并k个链表 维护一个优先队列 优先队列里为k个链表的头节点
# 每次抽出最小的一个，并将其下一个节点加入优先队列
from heapq import *
ListNode.__lt__ = lambda a, b: a.val < b.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        h = [head for head in lists if head]
        heapify(h)
        while h:
            node = heappop(h)
            if node.next:
                heappush(h, node.next)
            cur.next = node
            cur = cur.next
        return dummy.next
        
# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()