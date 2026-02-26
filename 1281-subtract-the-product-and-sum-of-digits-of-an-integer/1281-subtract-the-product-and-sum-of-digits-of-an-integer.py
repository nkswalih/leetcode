class Solution(object):
    def subtractProductAndSum(self, n):
        product=1
        sum=0

        for i in str(n):
            sum += int(i)
            product *= int(i)
        
        return product-sum
        