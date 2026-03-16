class Solution(object):
    def countCharacters(self, words, chars):
        res=0
        for word in words:
            temp=list(chars)
            good = True

            for ch in word:
                if ch in temp:
                    temp.remove(ch)
                else:
                    good = False
                    break
            if good:
                res += len(word)
        return res