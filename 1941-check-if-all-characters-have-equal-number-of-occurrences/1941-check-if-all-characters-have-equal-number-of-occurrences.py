class Solution(object):
    def areOccurrencesEqual(self, s):
        freq = {}
        res = False
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
            
        values = list(freq.values())
        first = values[0]

        for v in values:
            if v != first:
                return False
        return True