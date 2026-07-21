class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        counts = [0] * 128
        for char in t:
            counts[ord(char)] += 1
        missing = len(t)
        min_len = float('inf')
        best_left = 0
        left = 0
        for right, char in enumerate(s):
            char_code = ord(char)
            if counts[char_code] > 0:
                missing -= 1
            counts[char_code] -= 1
            if missing == 0:
                while True:
                    left_code = ord(s[left])
                    if counts[left_code] == 0:
                        break  
                    counts[left_code] += 1
                    left += 1
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    best_left = left
                counts[ord(s[left])] += 1
                missing += 1
                left += 1    
        return "" if min_len == float('inf') else s[best_left : best_left + min_len]



                                         (or)

  from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        t_counts = Counter(t)
        required = len(t_counts)
        filtered_s = [(i, char) for i, char in enumerate(s) if char in t_counts]
        window_counts = {}
        formed = 0
        left = 0
        min_len = float('inf')
        best_left = 0
        best_right = 0
        for right, (orig_idx, char) in enumerate(filtered_s):
            window_counts[char] = window_counts.get(char, 0) + 1
            if window_counts[char] == t_counts[char]:
                formed += 1
            while left <= right and formed == required:
                start_idx = filtered_s[left][0]
                end_idx = orig_idx
                if end_idx - start_idx + 1 < min_len:
                    min_len = end_idx - start_idx + 1
                    best_left = start_idx
                    best_right = end_idx
                left_char = filtered_s[left][1]
                window_counts[left_char] -= 1
                if window_counts[left_char] < t_counts[left_char]:
                    formed -= 1 
                left += 1
        return "" if min_len == float('inf') else s[best_left : best_right + 1]

                                              (or)

  class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        t_counts = [0] * 128
        for char in t:
            t_counts[ord(char)] += 1
        required = sum(1 for count in t_counts if count > 0)
        window_counts = [0] * 128
        formed = 0
        left = 0
        min_len = float('inf')
        best_left = 0
        for right, char in enumerate(s):
            char_code = ord(char)
            window_counts[char_code] += 1
            if t_counts[char_code] > 0 and window_counts[char_code] == t_counts[char_code]:
                formed += 1
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    best_left = left
                left_char_code = ord(s[left])
                window_counts[left_char_code] -= 1
                if t_counts[left_char_code] > 0 and window_counts[left_char_code] < t_counts[left_char_code]:
                    formed -= 1
                left += 1
        return "" if min_len == float('inf') else s[best_left : best_left + min_len]
