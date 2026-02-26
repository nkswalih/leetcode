class Solution(object):
    def largestOddNumber(self, num):
        while num:
            if int(num[-1]) % 2 == 1:
                return num
            num = num[:-1]
        return ""