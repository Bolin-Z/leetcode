# 题目：138.随机链表的复制
# 标签：哈希 链表
# 难度：中等
# 日期：12.19

from typing import *

# 思路:
# 在原链表和新链表中做同样的动作 直到 cur = random

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
    #     dummy = Node(0)
    #     cur, new_cur = head, dummy
    #     while cur:
    #         new_cur.next = Node(x=cur.val)
    #         new_cur = new_cur.next
    #         cur = cur.next
    #     cur, new_cur = head, dummy.next
    #     while cur:
    #         if cur.random: # find
    #             find_ptr, find_new_ptr = head, dummy.next
    #             while find_ptr != cur.random:
    #                 find_ptr = find_ptr.next
    #                 find_new_ptr = find_new_ptr.next
    #             new_cur.random = find_new_ptr
    #         cur = cur.next
    #         new_cur = new_cur.next
    #     return dummy.next

# 灵山 采用奇偶链表的方式
# 1->1'->2->2'->3->3' 然后再分离
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        
        # 复制 1->2->3 
        # 1->1'->2->2'->3->3'
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next
        
        # 设置 random 指针
        cur = head
        while cur:
            if cur.random:
                copy_node, copy_random = cur.next, cur.random.next
                copy_node.random = copy_random
            cur = cur.next.next

        # 分开交错链表 1->1'->2->2'->3->3'
        # 1->2->3 1'->2'->3'
        new_head = head.next
        cur = head
        while cur.next.next: # 1->1'->2
            copy = cur.next
            cur.next = copy.next # 1->2
            copy.next = copy.next.next # 1'->2'
            cur = cur.next # cur -> 2
        cur.next = None
        return new_head

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