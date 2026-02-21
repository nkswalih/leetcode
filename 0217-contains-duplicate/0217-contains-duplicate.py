class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        f = False
        for i in nums:
            if i in s:
                f = True
            else:
                s.add(i)
        return f
        