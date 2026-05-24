class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the last seen index of each character
        max_length = 0
        left = 0  # Left boundary of the sliding window

        for right in range(len(s)):
            # If the character is already in the window, shrink the window
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1

            # Update the last seen position of the character
            char_map[s[right]] = right

            # Calculate the current window size and update max_length
            max_length = max(max_length, right - left + 1)

        return max_length
