class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)): #for remove useless checks
            substring = haystack[i : i + len(needle)]
            if substring == needle:
                return i
        
        return -1