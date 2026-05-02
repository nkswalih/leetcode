class Solution(object):
    def rotatedDigits(self, n: int) -> int:
        good_count = 0
        
        # 'Good' digits that force the number to change
        changers = {'2', '5', '6', '9'}
        # 'Invalid' digits that break the number
        invalid = {'3', '4', '7'}
        
        for i in range(1, n + 1):
            s = str(i)
            # Check if any digit is in the 'invalid' set
            # set.intersection is a very fast DSA trick
            has_invalid = any(d in invalid for d in s)
            
            if not has_invalid:
                # If it's safe, it must have at least one 'changer' 
                # to be different from the original number
                if any(d in changers for d in s):
                    good_count += 1
                    
        return good_count