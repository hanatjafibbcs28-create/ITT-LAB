class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        current_str = "1"
        
        # Generate the sequence up to n iteratively
        for _ in range(1, n):
            next_str_chars = []
            i = 0
            length = len(current_str)
            
            # Step through the current string to group identical characters
            while i < length:
                count = 1
                # Count consecutive matching characters
                while i + 1 < length and current_str[i] == current_str[i + 1]:
                    count += 1
                    i += 1
                
                # Append the count followed by the digit itself
                next_str_chars.append(str(count))
                next_str_chars.append(current_str[i])
                i += 1
                
            # Update current_str for the next iteration
            current_str = "".join(next_str_chars)
            
        return current_str
