# 题目：202.快乐数
# 标签：哈希 数学 双指针
# 难度：简单
# 日期：12.17

from typing import *

# 思路:
# 用一个哈希表存储已经出现的结果，如果重新出现说明就会陷入循环
# 会不会无限不循环？
# 数 x 的位数为 m 则有
# x < 10^{m} x' <= 81m
# 10{m - 1} >= 81m 时位数缩短 m >= 4 时成立
# 所以长度会缩短 说明结果有限 -> 不会无限不循环

class Solution:
    def isHappy(self, n: int) -> bool:
        sq = {i:i ** 2 for i in range(10)}
        table = set()
        while n != 1:
            sum = 0
            while n > 0:
                sum += sq[(n % 10)]
                n //= 10
            if sum in table:
                return False
            table.add(sum)
            n = sum
        return True

    def test(self):
        """test code
        """
        test_cases = [
            [19],[2]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.isHappy(case[0])
            if type(answer) == List:
                for ans in answer:
                    print(f"\t\t{ans}")
            else:
                print(f"\t\t{answer}")


# 官方题解
# 快慢指针法
# 只有两种情况：存在循环，到达1
# 存在循环的时候，快指针每次走2 满指针走1 肯定会遇上
# 不存在的时候 快指针先到达1
class Solution:
    def isHappy(self, n: int) -> bool:
        fast = slow = n
        while fast != 1:
            fast = self.go_next(self.go_next(fast))
            slow = self.go_next(slow)
            if fast == slow and fast != 1:
                return False
        return True

    def go_next(self, n:int) -> int:
        sq = {i:i ** 2 for i in range(10)}
        sum = 0
        while n > 0:
            sum += sq[n % 10]
            n //= 10
        return sum

# 数学方法
# 肯定会掉入小于 243 的范围内 小于这个数的x的各位平方和一定小于243
# 通过暴力分析，可以得到所有循环的都会在 4→16→37→58→89→145→42→20→4
# 或者抵达 1
class Solution:
    def isHappy(self, n: int) -> bool:
        cycle_num = {4,16,37,58,89,145,42,20,4}
        sq = {i:i ** 2 for i in range(10)}
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += sq[digit]
            return total_sum
        while n != 1 and n not in cycle_num:
            n = get_next(n)
        return n == 1

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()