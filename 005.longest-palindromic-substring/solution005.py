# 方法一：暴力破解法
# 思路： 写一个func，判断某个子列是否是回文子串，然后遍历s的所有子列即可判断


# 方法二：动态规划法

"""
思路：
1. 状态转移方程：
定义dp[i][j]为判断子列s[i,j]是否是回文子串；
所以dp[i-1][j+1]可以用dp[i][j]进行表示
2. 边界条件
dp[i][i] = 1
dp[i][i+1] = (s[i]==s[i+1])
3. 最终结果
对于所有判断为回文子串的序列，取出s[i:j+1]，找到最长的进行输出

注意：i<=j，所以这个动态规划表格只有一半
"""
# 这个方法太慢了
import numpy as np
class Solution(object):
    def longestPalindrome(self, s):
        l = len(s)
        if l == 1:
            return s
        elif l == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            dp = np.zeros((l, l))
            i = list(range(l))
            # 给边界值赋值
            dp[i, i] = 1
            s_max = s[0:1]
            maxLen = 1
            for i in range(l-1):
                j = i+1
                if s[i] == s[j]:
                    dp[i][j] = 1
                    maxLen = 2
                    s_max = s[i:j+1]
            # 动态规划，利用转移函数计算出各个状态值
            for k in range(3, l + 1):  # 从长度为3的子串开始计算
                for i in range(l-k+1):
                    j = i+k-1
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                        if dp[i][j] == 1:
                            sublen = k
                            if sublen > maxLen:
                                maxLen = sublen
                                s_max = s[i:j+1]
        return s_max

# 方法三： manacher算法
# 线性时间就能解决回文问题，链接：https://segmentfault.com/a/1190000008484167