from collections import defaultdict

class Solution(object):
    def distance(self, nums):
        groups = defaultdict(list)
        
        # Step 1: group indices
        for i, num in enumerate(nums):
            groups[num].append(i)
        
        res = [0] * len(nums)
        
        # Step 2: process each group
        for indices in groups.values():
            n = len(indices)
            
            # prefix sum
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i+1] = prefix[i] + indices[i]
            
            # compute result
            for i in range(n):
                idx = indices[i]
                
                # left contribution
                left = i * idx - prefix[i]
                
                # right contribution
                right = (prefix[n] - prefix[i+1]) - (n - i - 1) * idx
                
                res[idx] = left + right
        
        return res