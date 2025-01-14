/* 题目: 139.单词拆分
 * 标签: 
 * 难度: 中等
 * 日期: 1.10
 */

/* 思路:
// 
//
 */

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class t139 {
    public boolean wordBreak(String s, List<String> wordDict) {
        int maxWordLen = Integer.MIN_VALUE;
        int minWordLen = Integer.MAX_VALUE;
        HashSet<String> wordSet = new HashSet<>();
        for (String word : wordDict){
            maxWordLen = Math.max(maxWordLen, word.length());
            minWordLen = Math.min(minWordLen, word.length());
            wordSet.add(word);
        }
        boolean[] matchprefix = new boolean[s.length() + 1];
        matchprefix[0] = true;
        for(int endIndex = 0; endIndex < s.length(); endIndex++){
            for (int beginIndex = endIndex - maxWordLen + 1; beginIndex <= endIndex - minWordLen + 1; beginIndex++){
                if (beginIndex >= 0 && beginIndex < s.length() && matchprefix[beginIndex]){
                    String subStr = s.substring(beginIndex, endIndex + 1);
                    if (wordSet.contains(subStr)){
                        matchprefix[endIndex + 1] = true;
                        break;
                    }
                }
            }
        }
        return matchprefix[s.length()];
    }
    public static void main(String[] args) {
        String s = "leetcode";
        List<String> wordDict = Arrays.asList("leet","code");
        t139 solver = new t139();
        solver.wordBreak(s, wordDict);
    }
}
