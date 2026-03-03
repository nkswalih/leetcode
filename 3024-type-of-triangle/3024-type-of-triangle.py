class Solution(object):
    def triangleType(self, nums):
        nums.sort()
        if not nums[0] + nums[1] > nums[2]:
            return "none"
        triangle = len(set(nums))
        if triangle == 1:
            return "equilateral"
        elif triangle == 2:
            return "isosceles"
        else:
            return "scalene"