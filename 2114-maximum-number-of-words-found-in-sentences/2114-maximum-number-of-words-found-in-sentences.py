class Solution(object):
    def mostWordsFound(self, sentences):
        length = 0
        for sentence in sentences:
            words = sentence.split()
            if len(words) > length:
                length=len(words)
            
        return length