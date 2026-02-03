class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1
        
# I’m using a hash map to store character frequency, then scanning again to find the first character with frequency one.