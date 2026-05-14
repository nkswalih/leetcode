class Solution(object):
    def recoverOrder(self, order, friends):
        res = []
        for num in order:
            for friend in friends:
                if num == friend:
                    res.append(num)
        return res