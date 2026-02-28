class Solution(object):
    def checkZeroOnes(self, s):
        max1 = 0
        max0 = 0
        count1 = 0
        count0 = 0
        for i in s:
            if i == "1":
                count1+=1
                count0=0
                max1 = max(max1, count1)
            
            else:
                count0+=1
                count1=0
                max0 = max(max0, count0)
        return max1 > max0
        