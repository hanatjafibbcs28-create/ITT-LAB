class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0
        star_idx = -1
        s_match = 0
        s_len, p_len = len(s), len(p)
        
        while s_ptr < s_len:
            # 1. Direct match or '?' wildcard
            if p_ptr < p_len and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            # 2. Encountered a '*' wildcard: save state and try empty match
            elif p_ptr < p_len and p[p_ptr] == '*':
                star_idx = p_ptr
                s_match = s_ptr
                p_ptr += 1
            # 3. Mismatch: backtrack to the last '*' and consume 1 character from s
            elif star_idx != -1:
                p_ptr = star_idx + 1
                s_match += 1
                s_ptr = s_match
            # 4. Total mismatch with no '*' fallback
            else:
                return False
                
        # Consume any remaining trailing asterisks
        while p_ptr < p_len and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == p_len
