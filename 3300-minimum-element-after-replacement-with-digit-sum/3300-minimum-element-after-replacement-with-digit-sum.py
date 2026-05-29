class Solution:

    def minElement(self, nums: list[int]) -> int:
        # Calculate the sum of digits for each number and find the minimum
        return min(sum(int(digit) for digit in str(num)) for num in nums)
