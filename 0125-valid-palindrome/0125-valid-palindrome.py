class Solution(object):
    def isPalindrome(self, s):
        cleaned = ''
        for ch in s.lower():
            if ch.isalnum():
                cleaned += ch
    
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False

    
        