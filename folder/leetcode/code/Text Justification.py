class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        n = len(words)
        i = 0
        while i < n:
            line_words = [words[i]]
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + len(line_words) + len(words[j]) <= maxWidth:
                line_words.append(words[j])
                line_len += len(words[j])
                j += 1
            if j == n or len(line_words) == 1:
                left_justified = " ".join(line_words)
                res.append(left_justified + " " * (maxWidth - len(left_justified)))
            else:
                total_spaces = maxWidth - line_len
                gaps = len(line_words) - 1        
                base_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                line_parts = []
                for k in range(gaps):
                    line_parts.append(line_words[k])
                    line_parts.append(" " * (base_spaces + (1 if k < extra_spaces else 0)))
                line_parts.append(line_words[-1])
                res.append("".join(line_parts))
            i = j
            
        return res
