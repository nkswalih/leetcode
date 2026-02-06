class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        f = 0
        s = str(x)
        for i in s:
            f += int(i)
        if x % f == 0:
            return f
        else:
            return -1
        