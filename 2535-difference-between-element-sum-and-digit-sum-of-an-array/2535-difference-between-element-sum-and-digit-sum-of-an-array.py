class Solution(object):
    def differenceOfSum(self, nums):
        element_sum = 0
        digit_sum = 0
        for num in nums:
            element_sum += num
            for j in str(num):
                digit_sum += int(j)
        return abs(element_sum - digit_sum)

        