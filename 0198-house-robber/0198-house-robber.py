class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev2 = 0  # Max loot up to house i-2
        prev1 = 0  # Max loot up to house i-1

        for num in nums:
            # Decide whether to rob current house + prev2 OR keep prev1
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1