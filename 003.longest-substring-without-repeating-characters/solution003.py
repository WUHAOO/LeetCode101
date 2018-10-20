
'''
##  - 暴力破解法 -

# 遍历string的所有子列，for i in range(len(s): for j in range(i+1.len(s)),
# 检查子列是不是unique，如果是，记录长度，和目前最大值进行比较；如果不是，不记录
# 时间复杂度为O(n^3)
def unique(s):
    hashSet = set()
    flag = True
    for i in s:
        if i in hashSet:
            flag = False
        else:
            hashSet.add(i)
    return flag


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                subString = s[i:j]
                if unique(subString):
                    maxLen = max(maxLen, len(subString))
        return maxLen

'''


'''
## - 方法二 sliding window - 
# 利用hashSet提高一部分时间，还是慢的令人发指，只超过了6.67%的人..

def maxUnique(s):
    hashSet = set()
    for x in s:
        if x in hashSet:
            return len(hashSet)
        else:
            hashSet.add(x)
    return len(hashSet)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # 主要可以节省时间的地方在于，如果我们已经判断一个长子列是unique的，下一次遇到这个子列的子列就不需要再做判断
        # 如果我们维护一个已经确认是unique的子列为hashSet，然后遇到这个子列的扩展时，我们可以以O(1)的时间知道，新加入的元素是否在原子列中
        maxLen = 0
        for i in range(len(s)):
            subString = s[i:]
            l = maxUnique(subString)
            maxLen = max(maxLen,l)
        return maxLen
'''
## - 方法三 维护两个hashTable -
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        FirstPosition = dict()  # 某个字母开始位置
        startPosition = 1  # 目前查找的段落开始位置
        maxLen = 0
        print (s)
        for i in range(len(s)):
            x = s[i]
            i = i + 1
            if x in FirstPosition:
                fp = FirstPosition[x]
                if startPosition <= fp:
                    startPosition = fp + 1
                    FirstPosition[x] = i
            FirstPosition[x] = i
            maxLen = max(maxLen, i - startPosition+1)
            print ('i:',i,' x:',x)
            print ('Len:', i - startPosition+1)
            print ('FirstPosition:',FirstPosition)
            print ('startPosition:',startPosition)
            print ('max:',maxLen)
        return maxLen

