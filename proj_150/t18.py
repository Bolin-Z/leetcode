# 题目：12.整数转罗马数字
# 标签：哈希表 数学 字符串
# 难度：中等

from typing import *

# 思路:
#

class Solution:
    def intToRoman(self, num: int) -> str:
        hash_table = {
            1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:"IV", 1:'I'
        }
        test_number = [
            1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
        ]
        ans_list = []
        test_idx = 0
        while num > 0:
            if num - test_number[test_idx] >= 0:
                num -= test_number[test_idx]
                ans_list.append(hash_table[test_number[test_idx]])
            else:
                test_idx += 1
        return ''.join(ans_list)

    def test(self):
        """test code
        """
        test_cases = [
            3749, 58, 1994
        ]
        for i, n in enumerate(test_cases):
            print(f"测试用例{i + 1}:")
            print(f"\t输入: num = {n}")
            print(f"\t输出: {self.intToRoman(n)}")

# 官方题解
# 更加暴力的解法，因为输入范围有限 [1, 3999]直接拆分成各十百千位
class Solution:

    THOUSANDS = ["", "M", "MM", "MMM"]
    HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    def intToRoman(self, num: int) -> str:
        return Solution.THOUSANDS[num // 1000] + \
            Solution.HUNDREDS[num % 1000 // 100] + \
            Solution.TENS[num % 100 // 10] + \
            Solution.ONES[num % 10]


# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()