from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map to store { character_count_tuple : [list of anagrams] }
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Create a frequency count array for lowercase English letters (a-z)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Convert list to tuple so it can be used as a dictionary key
            anagram_map[tuple(count)].append(s)
            
        # Return all grouped anagram lists
        return list(anagram_map.values())
