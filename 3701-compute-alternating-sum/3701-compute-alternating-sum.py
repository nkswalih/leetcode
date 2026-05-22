class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        alt = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                alt += nums[i]
            if i % 2 == 1:
                alt -= nums[i]
        return alt
        