class Solution(object):
    def minimumOperations(self, nums):
        operations = 0
        
        for num in nums:
            # If the number is not divisible by 3, it takes 1 operation
            if num % 3 != 0:
                operations += 1
                
        return operations
        