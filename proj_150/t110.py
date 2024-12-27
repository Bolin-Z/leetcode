# 题目：148.排序链表 *
# 标签：链表 双指针 分治排序 归并
# 难度：中等
# 日期：12.26

from typing import *

# 思路:
# 排序好剩下的，然后插入 (TLE)
# 对每一个节点，摘出来，将剩下的节点分为大于这个节点和小于这个节点的，再分别排序 (TLE)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:Optional[ListNode] = next

class Solution:
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head == None:
    #         return None
    #     if head.next == None: # 最后一个节点
    #         return head
    #     new_head = self.sortList(head.next)
    #     p1, p2 = None, new_head
    #     while p2 and p2.val < head.val:
    #         p1 = p2
    #         p2 = p2.next
    #     if p1 is None:
    #         head.next = new_head
    #         new_head = head
    #     else:
    #         p1.next = head
    #         head.next = p2
    #     return new_head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head: Optional[ListNode]) -> List[ListNode]:
            if head == None or head.next == None:
                return [head, head]
            shead, stail, lhead, ltail = None, None, None, None
            ptr:ListNode = head.next
            while ptr:
                nxt = ptr.next
                if ptr.val > head.val:
                    ptr.next = lhead
                    lhead = ptr
                    if ltail is None:
                        ltail = ptr
                else:
                    ptr.next = shead
                    shead = ptr
                    if stail is None:
                        stail = ptr
                ptr = nxt
            shead, stail = helper(shead)
            lhead, ltail = helper(lhead)
            head.next = lhead
            if stail:
                stail.next = head
            new_head = shead if shead else head
            new_tail = ltail if ltail else head
            return [new_head, new_tail]
        ans, _ = helper(head)
        return ans


    def test(self):
        nodes = [ListNode(i) for i in [4, 2, 1, 3]]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        self.sortList(nodes[0])

# 官方题解
# 归并排序
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head # 快慢指针找到中间节点
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None # 断开
        return mid
    
    def mergeTwoLists(self, list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode() # 哨兵节点
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2 # 链接剩下链表
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: # 一个节点或空
            return head
        # 找到中间节点断开
        head2 = self.middleNode(head)
        # 分治
        head = self.sortList(head)
        head2 = self.sortList(head2)
        # 合并
        return self.mergeTwoLists(head, head2)

# 归并排序 迭代版
class Solution:
    def getListLength(self, head:Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def splitList(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        # 拆分size个节点出来并返回下一个头部
        cur = head
        for _ in range(size - 1):
            if cur is None:
                break
            cur = cur.next
        if cur is None or cur.next is None:
            return None
        next_head = cur.next
        cur.next = None # 断开
        return next_head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Tuple[ListNode, ListNode]:
        # 合并两个链表并返回头尾节点
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2 # 拼接
        while cur.next: # 找结尾
            cur = cur.next
        return dummy.next, cur

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getListLength(head)
        dummy = ListNode(next=head)
        step = 1
        while step < length:
            new_list_tail = dummy
            cur = dummy.next
            while cur:
                head1 = cur
                head2 = self.splitList(head1, step)
                cur = self.splitList(head2, step)
                head, tail = self.mergeTwoLists(head1, head2)
                new_list_tail.next = head
                new_list_tail = tail
            step *= 2
        return dummy.next


# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()