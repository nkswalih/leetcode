class Solution(object):
    def minimumDistance(self, nums):
        mp = {}
        for i, num in enumerate(nums):
            if num not in mp:
                mp[num] = []
            mp[num].append(i)

        ans = float('inf')

        for indices in mp.values():
            if len(indices) < 3:
                continue
            
            for i in range(len(indices) - 2):
                left = indices[i]
                right = indices[i+2]

                distance = 2 * (right - left)

                ans = min(ans, distance)
        return ans if ans != float('inf') else -1