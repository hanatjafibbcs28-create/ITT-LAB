class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                
            elif char in ('+', '-'):
                # Signs can only appear at index 0 or immediately after an exponent 'e'/'E'
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
                    
            elif char in ('e', 'E'):
                # Exponent can only appear once, and must follow at least one digit
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False  # Reset to ensure an integer follows the exponent
                
            elif char == '.':
                # Dot can only appear once and cannot appear after an exponent
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
                
            else:
                # Any other character (like alphabets or special symbols) makes it invalid
                return False
                
        # The string is valid only if it ends with a valid digit sequence
        return seen_digit
