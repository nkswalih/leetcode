class Solution(object):
    def countConsistentStrings(self, allowed, words):
        res = 0
        for word in words:
            for ch in word:
                if ch not in allowed:
                    break
            else:
                res+=1
        return res