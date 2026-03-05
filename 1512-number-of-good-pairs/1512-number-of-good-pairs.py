class Solution(object):
    def numIdenticalPairs(self, nums):
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if i < j and nums[i] == nums[j]:
                    res += 1
        return res
        