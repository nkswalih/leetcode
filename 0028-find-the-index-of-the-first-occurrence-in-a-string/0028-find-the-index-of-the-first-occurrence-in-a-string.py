class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            substring = haystack[i : i + len(needle)]
            if substring == needle:
                return i
        
        return -1