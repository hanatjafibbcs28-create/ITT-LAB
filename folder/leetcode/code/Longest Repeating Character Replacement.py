class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}
        left = 0
        max_freq = 0
        max_length = 0
        for right in range(len(s)):
            char_counts[s[right]] = char_counts.get(s[right], 0) + 1
            max_freq = max(max_freq, char_counts[s[right]])
            if (right - left + 1) - max_freq > k:
                char_counts[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
