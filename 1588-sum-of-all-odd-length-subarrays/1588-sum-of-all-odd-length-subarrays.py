class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            # Total subarrays that include the current element
            total_subarrays = (i + 1) * (n - i)
            
            # Number of odd-length subarrays containing this element
            odd_subarrays = (total_subarrays + 1) // 2
            
            # Add the contribution of the element to the total sum
            total_sum += odd_subarrays * arr[i]
            
        return total_sum
