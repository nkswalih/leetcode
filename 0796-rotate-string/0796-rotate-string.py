class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        b = s+s
    
        if goal.lower() in b.lower():
            return True
        else:
            return False
        