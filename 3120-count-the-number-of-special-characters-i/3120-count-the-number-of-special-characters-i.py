class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        unique_chars = set(word)
        special_count = 0
        
        for char in unique_chars:
            if char.islower() and char.upper() in unique_chars:
                special_count += 1
                
        return special_count
