class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        current_f = 0
        for i in range(n):
            current_f += i * nums[i]

            max_f = current_f

        for i in range(1, n):
            jumber = nums[n - i]
            current_f = current_f + total_sum - (n * jumber)
            if current_f > max_f:
                max_f = current_f

        return max_f
