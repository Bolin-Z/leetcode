from typing import List, Deque
from collections import deque

class TreeNode:
    def __init__(self, id:int) -> None:
        self.id = id
        self.parent:"TreeNode" = None
        self.children:List["TreeNode"] = []
        self.lockedUser = None

class LockingTree:

    def __init__(self, parent: List[int]):
        self.tree = [TreeNode(i) for i in range(len(parent))]
        for i in range(1, len(parent)):
            curNode = self.tree[i]
            parentNode = self.tree[parent[i]]
            curNode.parent = parentNode
            parentNode.children.append(curNode)

    def lock(self, num: int, user: int) -> bool:
        if self.tree[num].lockedUser == None:
            self.tree[num].lockedUser = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.tree[num].lockedUser == user:
            self.tree[num].lockedUser = None
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.tree[num].lockedUser == None:
            # check locked ancestors
            curNode = self.tree[num].parent
            while curNode:
                if curNode.lockedUser != None:
                    return False
                curNode = curNode.parent
            # check children
            query:Deque["TreeNode"] = deque()
            query.append(self.tree[num])
            flag = False
            while len(query) != 0:
                curNode = query.popleft()
                if curNode.lockedUser:
                    flag = True
                    curNode.lockedUser = None
                for cnode in curNode.children:
                    query.append(cnode)
            if not flag:
                return False
            # locked current node
            self.tree[num].lockedUser = user
            return True
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)