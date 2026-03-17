class Solution(object):
    def runningSum(self, nums):
        runningSum = []
        currentTotal = 0
        for i in nums:
            currentTotal += i
            runningSum.append(currentTotal)
        return runningSum