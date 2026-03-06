class Solution(object):
    def countDigits(self, num):
        res = 0
        for i in str(num):
            if num % int(i) == 0:
                res += 1
        return res
        