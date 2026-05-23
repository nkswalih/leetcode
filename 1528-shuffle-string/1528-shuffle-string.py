class Solution(object):
    def restoreString(self, s, indices):
        res = [''] * len(s)
        for i,ch in enumerate(s):
            res[indices[i]] = ch
        return "".join(res)
        