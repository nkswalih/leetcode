class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) > 15:
            return
    
        r = {
        "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
        }
        
        total = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and r[s[i]] < r[s[i+1]]:
                total -= r[s[i]]
            else:
                total += r[s[i]]
        
        return total