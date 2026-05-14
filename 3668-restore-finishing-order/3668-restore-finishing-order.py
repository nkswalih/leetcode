class Solution(object):
    def recoverOrder(self, order, friends):
        friends_set = set(friends)
        res = []
        for num in order:
            if num in friends:
                res.append(num)
        return res