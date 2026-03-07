class Solution(object):
    def areOccurrencesEqual(self, s):
        freq = {}
        res = False
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
            
        return len(set(freq.values())) == 1