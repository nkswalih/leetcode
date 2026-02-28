class Solution(object):
    def findDifference(self, nums1, nums2):
        first = set(nums1)
        second = set(nums2)
        return [list(first - second), list(second - first)]
        