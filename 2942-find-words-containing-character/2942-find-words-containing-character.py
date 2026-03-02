class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for i in range(len(words)):
            for ch in words[i]:
                if ch == x:
                    res.append(i)
                    break
        return res
        