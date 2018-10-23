import numpy as np
"""
# 一个容易犯的错误
class Solution(object):
    def longestPalindrome(self, s):
        l = len(s)
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
        for i in range(l-1):
            for j in range(i+1, l):  # 这里犯了一个很容易犯的错误。要计算的现在的状态，必须是前面的状态已经计算过的。对于这个程序，abcba这个case检验时胡出错。因为先计算了i=0，j=4的情况，再计算i = 1，j = 3的情况，顺序有误。
                if j!=i+1:
                    print (i,j)
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                        if dp[i][j] == 1:
                            sublen = j-i+1
                            if sublen > maxLen:
                                maxLen = sublen
                                s_max = s[i:j+1]
        return s_max

"""