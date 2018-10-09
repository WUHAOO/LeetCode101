class Solution(object):
    def twoSum(self, nums, target):
        hashtable = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in hashtable:
                return [hashtable[n], i]
            target_n = target-n
            hashtable[target_n] = i

    # more decent version
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):  # 用enumerate， 直接就能取到index和value
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
