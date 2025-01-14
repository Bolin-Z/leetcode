/* 题目: 5.最长回文子串 **
 * 标签: 
 * 难度: 中等
 * 日期: 1.11
 */

/* 思路: 感觉有点像kmp
 * 1. 从中心向两边扩展
 * 2. Manacher算法
 */

public class t145 {

    public static void main(String[] args) {
        t145 solver = new t145();
        System.out.println(solver.longestPalindrome("cbbd"));
        System.out.println(solver.longestPalindrome("babad"));
    }

    public String longestPalindrome(String s) {
        // return Manacher(s);
        return BruteForce(s);
    }

    public String BruteForce(String s) {
        // O(n^2) 暴力解法
        char[] ss = s.toCharArray();
        int maxLen = 0;
        int startIdx = 0, endIdx = 0;
        for (int i = 0; i < ss.length; i++) {
            int len;
            // 以 i 为中心长度为奇数的回文串
            len = getLen(ss, i, i);
            if (len > maxLen) {
                maxLen = len;
                startIdx = i - (len >> 1);
                endIdx = i + (len >> 1) + 1;
            }
            // 以 i wei中心长度为偶数的回文串
            len = getLen(ss, i, i + 1);
            if (len > maxLen) {
                maxLen = len;
                startIdx = i - (len >> 1) + 1;
                endIdx = i + (len >> 1) + 1;
            }
        }
        return s.substring(startIdx, endIdx);
    }

    public int getLen(char[] ss, int left, int right) {
        while (left >= 0 && right < ss.length && ss[left] == ss[right]) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    public String Manacher(String s) {
        int n = s.length() * 2 + 1;
        // 拓展字符串
        // 拓展字符串中 偶数位置为原字符串字符, 奇数位置为 #
        // 转换有
        char[] ss = new char[n];
        for (int i = 0, j = 0; i < n; i++) {
            ss[i] = (i & 1) == 0 ? '#' : s.charAt(j++);
        }
        // p[i]表示以i为中心的回文串的半径
        int[] p = new int[n];
        // 最大的p[i]和对应的i
        int max = 0;
        int imax = 0;
        // 求 ss 字符串的 p 数组
        for (int i = 0, c = 0, r = 0; i < n; i++) {
            // 当前检查的中心是否有被包括在r内
            // 如果不包括，则 len 初始化为 1 进行中心扩展
            // 如果包括, 则有三种情况:
            // 1. i 关于 c 的对称点 i' 的回文串完全在 c 的回文串内部 则 p[i] = p[i']
            // 2. i 关于 c 的对称点 i' 的回文串超出 c 的回文串左边界 l 则 p[i] = r - i // 否则 c 的半径可以扩更大
            // 3. i 关于 c 的对称点 i' 的回文串刚好与 c 的回文串左边界 l 重合, 则需要对 i 进行中心扩展, 但可以从 r 开始
            int len = r > i ? Math.min(p[2 * c - i], r - i) : 1;
            while(i + len < n && i - len >= 0 && ss[i + len] == ss[i - len]) {
                // 中心拓展
                len++;
            }
            if (i + len > r) {
                // 新的中心 c 和边界 r
                r = i + len;
                c = i;
            }
            if (len > max) {
                // 更长的回文子串
                max = len;
                imax = i;
            }
            // 更新 p[i]
            p[i] = len;
        }
        int startIdx = ((imax - max + 2) - 1) >>> 1;
        int endIdx = ((imax + max - 2) - 1) >>> 1;
        return s.substring(startIdx, endIdx + 1);
    }
}
